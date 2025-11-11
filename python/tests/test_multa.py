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
    with pytest.raises(ValueError):
        calcular_multa(-1)