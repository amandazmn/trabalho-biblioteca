import time
import pytest
from src.biblioteca.repositorio import InMemoryRepo
from src.biblioteca.modelos import Livro, Usuario
from src.biblioteca.relogio import RelogioStub
from src.biblioteca.email_service import EmailServiceStub
from src.biblioteca.servico import BibliotecaService

@pytest.mark.slow
def test_operacao_rapida():
    repo = InMemoryRepo()
    repo.salvar_usuario(Usuario("u1","L"))
    repo.salvar_livro(Livro("l1","T", True))
    relogio = RelogioStub()
    email = EmailServiceStub()
    service = BibliotecaService(repo, email, relogio)
    t0 = time.perf_counter()
    service.emprestar("u1","l1")
    service.devolver("u1","l1")
    t1 = time.perf_counter()
    assert (t1 - t0) < 0.2
