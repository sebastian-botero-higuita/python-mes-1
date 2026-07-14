def calcular_impuesto(salario, porcentaje):
    """Calcula el valor del impuesto basado en un porcentaje (0 a 1).
    Lanza ValueError si los valores de entrada no son válidos.
    """
    # Primero asignamos mentalmente, luego validamos
    if salario < 0 or porcentaje < 0 or porcentaje > 1:
        raise ValueError("Los valores de entrada no son validos.")
    
    return salario * porcentaje