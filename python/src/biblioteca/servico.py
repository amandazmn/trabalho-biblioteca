def calcular_multa(dias_emprestimo: int) -> float:
    if dias_emprestimo <= 7:
        return 0.0
    return (dias_emprestimo - 7) * 2.0
