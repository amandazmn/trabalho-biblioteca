from datetime import date
from .modelos import Emprestimo

def calcular_multa(data_emprestimo: date, data_devolucao: date, dias_prazo: int = 7, multa_por_dia: float = 2.0) -> float:
    if data_devolucao < data_emprestimo:
        raise ValueError("Data de devolução anterior ao empréstimo")

    dias_atraso = (data_devolucao - data_emprestimo).days - dias_prazo
    if dias_atraso > 0:
        return dias_atraso * multa_por_dia
    return 0.0

class BibliotecaService:
    def __init__(self, repo, email_service=None, relogio=None):
        self.repo = repo
        self.email = email_service
        self.relogio = relogio

    def emprestar(self, usuario_id, livro_id):
        usuario = self.repo.usuarios[usuario_id]
        livro = self.repo.livros[livro_id]
        ativos = [
            e
            for e in self.repo.emprestimos
            if e.usuario_id == usuario_id and e.data_devolucao is None
        ]
        if len(ativos) >= usuario.limite:
            raise ValueError("Limite de empréstimos atingido")
        if not livro.disponivel:
            raise ValueError("Livro não disponível")
        livro.disponivel = False
        emp = Emprestimo(
            usuario_id=usuario_id,
            livro_id=livro_id,
            data_emprestimo=(self.relogio.hoje() if self.relogio else date.today()),
        )
        self.repo.salvar_emprestimo(emp)
        return emp

    def devolver(self, usuario_id, livro_id):
            for emp in self.repo.emprestimos:
                if emp.usuario_id == usuario_id and emp.livro_id == livro_id and emp.data_devolucao is None:
                    emp.data_devolucao = self.relogio.hoje() if self.relogio else date.today()
                    livro = self.repo.livros[livro_id]
                    livro.disponivel = True
                    dias = (emp.data_devolucao - emp.data_emprestimo).days
                    multa = calcular_multa(emp.data_emprestimo, emp.data_devolucao)
                    if multa > 0 and self.email:
                        self.email.enviar(
                            usuario_id,
                            "Multa por atraso",
                            f"Valor da multa: R${multa:.2f}",
                        )
                    return multa
            raise ValueError("Empréstimo não encontrado")