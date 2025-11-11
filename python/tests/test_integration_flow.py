from src.biblioteca.repositorio import InMemoryRepo
from src.biblioteca.modelos import Livro, Usuario
from src.biblioteca.relogio import RelogioStub
from src.biblioteca.email_service import EmailServiceStub
from src.biblioteca.servico import BibliotecaService

def test_fluxo_ponta_a_ponta():
    repo = InMemoryRepo()
    relogio = RelogioStub()
    email = EmailServiceStub()
    service = BibliotecaService(repo, email, relogio)
    repo.salvar_usuario(Usuario("u1","Carlos"))
    repo.salvar_livro(Livro("l1","O Aut", True))
    service.emprestar("u1","l1")
    relogio.avancar_dias(9)
    multa = service.devolver("u1","l1")
    assert multa == 4.0
    assert repo.livros["l1"].disponivel
    assert len(email.enviados) == 1
