# Importamos la funcion real que queremos poner a prueba 
import pytest # Obligatorio para poder usar pytest.raises
from operaciones import calcular_salario_neto

#========================================
# Bloque 1: CASOS EXITOSOS Y CASOS BORDE (Garantiza precision)
#========================================

def test_calculo_salario_correcto():
    """Caso exitoso: evalua que la suma de un salario y una bonificacion sea exacta."""
    # 1. Ejecutamos la funcion con datos de prueba controlados
    resultado_real = calcular_salario_neto(2000000, 500000)
    # 2. Hacemos la afirmacion matematica de lo que ESPERAMOS que de
    assert resultado_real == 2500000


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

#=====================================
# BLOQUE 2: CASOS ESCUDO (Garantizan seguridad con pytest.raises)
#=====================================

def test_salario_negativo_lanza_excepcion():
    """Caso escudo: Salario base negativo debe disparar ValueError."""
    with pytest.raises(ValueError) as informacion_error:
        calcular_salario_neto(-1000000, 200000)

# Verificamos que el mensaje del error sea exactamente el esperado
    assert str(informacion_error.value) == "Los valores financieros no pueden ser negativos"

def test_bonificacion_negativa_lanza_excepcion():
    """Caso escudo: Bonificacion negativa debe disparar ValueError."""
    with pytest.raises(ValueError) as informacion_error:
        calcular_salario_neto(2000000, -500000)
    
    assert str(informacion_error.value) == "Los valores financieros no pueden ser negativos"

def test_ambos_negativos_lanza_excepcion():
    """Caso escudo: Ambos parametros negativos deben disparar ValieError."""
    with pytest.raises(ValueError) as informacion_error:
        calcular_salario_neto(-1000000, -500000)

    assert str (informacion_error.value) == "Los valores financieros no pueden ser negativos"