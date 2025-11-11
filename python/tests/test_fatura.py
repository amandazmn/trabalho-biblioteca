import pytest
import time
from src.biblioteca.fatura_service import FaturaService
from src.biblioteca.repositorio import InMemoryFaturaRepository
from src.biblioteca.email_service import EmailServiceStub


class MockGatewayPagamento:
    def __init__(self, aprovar=True):
        self.aprovar = aprovar
        self.pagamentos = []

    def pagar(self, dados):
        self.pagamentos.append(dados)
        return {"status": "aprovado" if self.aprovar else "negado", "id": "123"}


@pytest.fixture
def service():
    repo = InMemoryFaturaRepository()
    email = EmailServiceStub()
    gateway = MockGatewayPagamento(aprovar=True)
    return FaturaService(repo, email, gateway)


@pytest.mark.parametrize(
    "dias_atraso, multa_por_dia, esperado",
    [(0, 2.0, 0.0), (2, 2.0, 4.0), (5, 1.5, 7.5)],
)
def test_calcular_multa_total_parametrizado(service, dias_atraso, multa_por_dia, esperado):
    assert service.calcular_multa_total(dias_atraso, multa_por_dia) == pytest.approx(esperado)


def test_excecao_dias_negativos(service):
    with pytest.raises(ValueError):
        service.calcular_multa_total(-1)


def test_envia_email_apos_pagamento_aprovado(service):
    service.registrar_pagamento_multa("u1", 3)
    assert service.email.enviados   
    enviado = service.email.enviados[0]
    assert "R$" in enviado["corpo"]


@pytest.mark.slow
def test_pagamento_deve_ser_rapido(service):
    t0 = time.perf_counter()
    service.registrar_pagamento_multa("u2", 1)
    assert (time.perf_counter() - t0) < 0.2


def test_integration_fluxo_pagamento_completo(service):
    resultado = service.registrar_pagamento_multa("u3", 4, multa_por_dia=2.5)
    faturas = service.repo.listar()

    assert resultado["status"] == "aprovado"
    assert len(faturas) == 1
    assert len(service.email.enviados) == 1

    email = service.email.enviados[0]
    assert "R$" in email["corpo"]
    assert "u3" in email["corpo"]
