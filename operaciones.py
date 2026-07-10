

def calcular_salario_neto(salario_base, bonificacion):
    """Calcula el salario neto sumando la bonificacion al salario base.
    Lanza ValueEroor si el salario base o la bonificacion son negativos."""
    if salario_base < 0 or bonificacion < 0:
        raise ValueError("Los valores financieros no pueden ser negativos")
    return salario_base + bonificacion