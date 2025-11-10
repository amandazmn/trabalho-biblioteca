import pytest
from src.biblioteca.servico import calcular_multa

@pytest.mark.parametrize("dias_emprestimo, esperado", [
    (7, 0.0),
    (8, 2.0),
    (10, 6.0),
])
def test_calcula_multa_parametrizado(dias_emprestimo, esperado):
    assert calcular_multa(dias_emprestimo) == pytest.approx(esperado)
