from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Livro:
    id: str
    titulo: str
    disponivel: bool = True


@dataclass
class Usuario:
    id: str
    nome: str
    limite: int = 3


@dataclass
class Emprestimo:
    usuario_id: str
    livro_id: str
    data_emprestimo: date
    data_devolucao: Optional[date] = None
