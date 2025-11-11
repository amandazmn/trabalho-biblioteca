from datetime import datetime
from .repositorio import InMemoryFaturaRepository
from .email_service import EmailServiceStub


class FaturaService:

    def __init__(self, repo=None, email=None, gateway=None):
        self.repo = repo or InMemoryFaturaRepository()
        self.email = email or EmailServiceStub()
        self.gateway = gateway

    def calcular_multa_total(self, dias_atraso: int, multa_por_dia: float = 2.0) -> float:
        if dias_atraso < 0:
            raise ValueError("Dias de atraso não pode ser negativo")
        return dias_atraso * multa_por_dia

    def registrar_pagamento_multa(self, usuario_id: str, dias_atraso: int, multa_por_dia: float = 2.0) -> dict:
        total = self.calcular_multa_total(dias_atraso, multa_por_dia)

        dados_pagamento = {
            "usuario_id": usuario_id,
            "valor": total,
            "data": datetime.now()
        }

        resultado = self.gateway.pagar(dados_pagamento) if self.gateway else {"status": "aprovado", "id": "0"}

        if resultado["status"] == "aprovado":
            self.repo.salvar({"usuario": usuario_id, "valor": total, "status": "pago"})
            assunto = "Pagamento de Multa da Biblioteca"
            corpo = f"Usuário {usuario_id}, multa paga com valor R${total:.2f}"
            self.email.enviar(usuario_id, assunto, corpo)

        return resultado
