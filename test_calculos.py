import pytest
from calculos import calcular_impuesto

# CONFIGURACION DE LA TABLA DE DATOS:
# 1.  le decimos a pytest los nombres de las variables que van a cambiar: "salario, porcentaje, resultado_esperado"
# 2. Le pasamos una lista de tuplas [(fila), (fila2), (fila3)] con los datos de prueba 
@pytest.mark.parametrize(
    "salario, porcentaje, resultado_esperado",
    [
        (2000000, 0.10, 200000), # Caso 1: impuesto del 10%
        (3000000, 0.20, 600000), # Caso 2: Impuesto del 20%
        (1500000, 0.00, 0),      # Caso 3: Caso borde (0% de impuesto )
        (0, 0.15, 0),            # Caso 4: Caso borde (SAlario en cero)
        (5000000, 0.19, 950000), #IVA Colombiano 19%
    ]
)
def test_calcular_impuesto_multiples_casos(salario, porcentaje, resultado_esperado):
    """ Un unico test que ejecutara automaticamente los 4 escenarios de la tabla superior."""

    resultado_real = calcular_impuesto(salario, porcentaje)
    assert resultado_real == resultado_esperado

#=================================================
# TEST DE ESCUDO - Parametrizados con pytest.raises
#===================================================
@pytest.mark.parametrize(
    "salario, porcentaje",
    [
        (-1000000, 0.10),   # Salario negativo
        (2000000, -0.10),   # Porcentaje negativo
        (2000000, 1.5),     # Porcentaje mayor a 1
        (-500000, -0.10),   # Ambos negativos
    ]
)
def test_valores_invalidos_lanzan_excepcion(salario, porcentaje):
    """Escudo parametrizado: valores invalidos deben disparar ValueError. """
    with pytest.raises(ValueError) as informacion_error:
        calcular_impuesto(salario, porcentaje)
        assert str(informacion_error.value) == "Los valores de entrada no son validos."