import pytest
from datetime import date, timedelta
from src.biblioteca.servico import calcular_multa

@pytest.mark.parametrize("dias_emprestimo, esperado", [
    (7, 0.0),
    (8, 2.0),
    (10, 6.0),
])
def test_calcula_multa_parametrizado(dias_emprestimo, esperado):
    data_emprestimo = date(2024, 1, 1)
    data_devolucao = data_emprestimo + timedelta(days=dias_emprestimo)
    assert calcular_multa(data_emprestimo, data_devolucao) == pytest.approx(esperado)

def test_calcula_multa_dias_negativos():
    data_emprestimo = date.today()
    data_devolucao = data_emprestimo - timedelta(days=1)
    with pytest.raises(ValueError, match="Data de devolução anterior ao empréstimo"):
        calcular_multa(data_emprestimo, data_devolucao)

def test_calcula_multa_sem_atraso():
    data_emprestimo = date.today()
    data_devolucao = data_emprestimo + timedelta(days=5)
    assert calcular_multa(data_emprestimo, data_devolucao) == 0.0
