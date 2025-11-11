from src.biblioteca.repositorio import InMemoryRepo
from src.biblioteca.modelos import Livro, Usuario
from src.biblioteca.relogio import RelogioStub
from src.biblioteca.email_service import EmailServiceStub
from src.biblioteca.servico import BibliotecaService

def test_devolver_e_gerar_multa_e_enviar_email():
    repo = InMemoryRepo()
    repo.salvar_usuario(Usuario("u1","Ana"))
    repo.salvar_livro(Livro("l1","T", True))
    relogio = RelogioStub()
    email = EmailServiceStub()
    service = BibliotecaService(repo, email, relogio)

    service.emprestar("u1","l1")
    relogio.avancar_dias(9)
    multa = service.devolver("u1","l1")
    assert multa == 4.0
    assert len(email.enviados) == 1
