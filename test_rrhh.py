import pytest
from rrhh import Empleado

#=============================================
# FIXTURES - Catalogo de moldes reutilizables
#=============================================

@pytest.fixture
def empleado_plantilla():
    """Fixture que crea un empleado estandar limpiro para los test."""
    return Empleado("Sebastian Botero", "Backend Developer", 3000000, 600000)

@pytest.fixture
def empleado_sin_bonificacion():
    """Fixture que crea un empleado con perfil de bonificacion cero."""
    return Empleado("Ana Gomez", "QA Engineer", 2500000, 0)

#==============================================
# BLOQUE 1: TEST DEL CAMINO FELIZ Y CASOS BORDE
#==============================================

def test_verificar_salario_neto(empleado_plantilla):
    """Prueba que el calculo del salario neto estandar sea exacto."""
    assert empleado_plantilla.calcular_salario_neto() == 3600000

def test_verificar_cargo(empleado_plantilla):
    """Prueba que el cargo se asigne correctamente en el objeto."""
    assert empleado_plantilla.cargo == "Backend Developer"

def test_verificar_nombre(empleado_plantilla):
    """Prueba que el nombre pertenezca intacto."""
    assert empleado_plantilla.nombre == "Sebastian Botero"

def test_salario_sin_bonificacion(empleado_sin_bonificacion):
    """Prueba caso borde: Si la bonificacion es cero, retorna solo el salario base."""
    assert empleado_sin_bonificacion.calcular_salario_neto() == 2500000

#========================================================
# BLOQUE 2: TEST DE ESCUDO  (Verificacion de Excepciones)
#========================================================

def test_salario_negativo_lanza_excepcion():
    """Escudo: intentar crear un empleado con salario negativo debe disparar ValueError."""
    with pytest.raises(ValueError) as informacion_error:
        Empleado("Pedro", "Dev", -1000000, 0)

    assert str(informacion_error.value) == "Los valores financieros no pueden ser negativos."

def test_bonificacion_negativa_lanza_excepcion():
    """Escudo Intentar crear un empleado con bonificacion negativa debe disparar ValueError."""
    with pytest.raises(ValueError) as informacion_error:
        Empleado("Pedro", "Dev", 3000000, -500000)

    assert str(informacion_error.value) == "Los valores financieros no pueden ser negativos."

    