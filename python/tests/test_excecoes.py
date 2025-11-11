import pytest
from src.biblioteca.repositorio import InMemoryRepo
from src.biblioteca.modelos import Livro, Usuario
from src.biblioteca.servico import BibliotecaService

def test_emprestar_livro_indisponivel_gera_excecao():
    repo = InMemoryRepo()
    repo.salvar_usuario(Usuario("u1","Ana"))
    repo.salvar_livro(Livro("l1","T", False))
    service = BibliotecaService(repo)
    with pytest.raises(ValueError, match="Livro não disponível"):
        service.emprestar("u1","l1")
