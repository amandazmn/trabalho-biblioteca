from typing import Dict, List
from .modelos import Livro, Usuario, Emprestimo


class InMemoryRepo:

    def __init__(self) -> None:
        self.livros: Dict[str, Livro] = {}
        self.usuarios: Dict[str, Usuario] = {}
        self.emprestimos: List[Emprestimo] = []

    def salvar_livro(self, livro: Livro) -> None:
        self.livros[livro.id] = livro

    def buscar_livro(self, livro_id: str) -> Livro | None:
        return self.livros.get(livro_id)

    def salvar_usuario(self, usuario: Usuario) -> None:
        self.usuarios[usuario.id] = usuario

    def buscar_usuario(self, usuario_id: str) -> Usuario | None:
        return self.usuarios.get(usuario_id)

    def salvar_emprestimo(self, emprestimo: Emprestimo) -> None:
        self.emprestimos.append(emprestimo)

    def listar_ativos(self, usuario_id: str) -> list[Emprestimo]:
        return [
            e for e in self.emprestimos
            if e.usuario_id == usuario_id and e.data_devolucao is None
        ]
    

class InMemoryFaturaRepository:

    def __init__(self):
        self._faturas = []

    def salvar(self, fatura: dict):
        self._faturas.append(fatura)

    def listar(self):
        return list(self._faturas)
