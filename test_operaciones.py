# Importamos la funcion real que queremos poner a prueba 
from operaciones import calcular_salario_neto

def test_calculo_salario_correcto():
    """Caso exitoso: evalua que la suma de un salario y una bonificacion sea exacta."""
    # 1. Ejecutamos la funcion con datos de prueba controlados
    resultado_real = calcular_salario_neto(2000000, 500000)

    # 2. Hacemos la afirmacion matematica de lo que ESPERAMOS que de
    assert resultado_real == 2500000

def test_calculo_salario_erroneo():
    """Caso Fallido Intencional: Forzamos un error para aprender a ler la terminal."""
    resultado_real = calcular_salario_neto(1000000, 200000)

    #Esto va a fallar a proposito porque 1.000.000 + 200.000 no da 1'500.000
    assert resultado_real == 15000000

def test_bonificacion_cero():
    """Caso borde: bonificación de cero debe retornar el salario base."""
    resultado = calcular_salario_neto(2000000, 0)
    assert resultado == 2000000


def test_salario_cero():
    """Caso borde: salario base cero con bonificación debe retornar la bonificación."""
    resultado = calcular_salario_neto(0, 500000)
    assert resultado == 500000


def test_valores_grandes():
    """Caso borde: valores grandes no deben perder precisión."""
    resultado = calcular_salario_neto(10000000, 5000000)
    assert resultado == 15000000