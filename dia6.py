# dia6.py - Laboratorio *args y ** kwargs | Día 6/180 | Hecho por: Sebas - Backend Jr en formacion

# === FUNCIONES MATEMATICAS FLEXIBLES ===

def sumar(*args):
    """Suma infinitos numeros. retorna 0 si no hay argumentos.
    args es TUPLA inmutable, no lista."""
    if not args:
        return 0
    try:
        return sum(args)
    except TypeError:
        return "Error: Todos los argumentos deben ser números."
    
def restar(*args):
        if not args:
            return 0
        try:
            primer_num = args[0]
            los_demas = args[1:]

            total = primer_num
            for num in los_demas:
                total -= num
            return total
        except TypeError:
            return "Error: solo se permiten numero"
def multiplicar(*args):
    if not args:
        return 0
    try:
        total = 1
        for num in args:
            total *= num
        return total
    except TypeError:
        return "Error: solo se permiten numero"

def promedio(*notas):
    if not notas:
        return 0
    total = sum(notas)
    cantidad = len(notas)
    return round(total / cantidad, 2) 

def registrar_api_endpoint(**kwargs):
    print("\n--- [API LOG] payload recibido ---")
    print(f"Tipo: {type(kwargs)}") #<class 'dict'>
    print(f"Datos: {kwargs}")

    nombre = kwargs.get("nombre", "Anonimo")  #.get evita que se rompa
    rol = kwargs.get("rol", "Usuario")
    print(f"Sistema: Reguistro exitoso para {nombre} [{rol}]")

        
# === ZONA DE PRUEBAS PARA VERIFICAR ===
if __name__ == "__main__":
    
    print("=== TEST 1: SUMAR *ARGS ===")
    print(f"sumar(5, 10, 15) = {sumar(5, 10, 15)}") # 30
    print(f"sumar() = {sumar()}") # 0
    
    print("\n=== TEST 2: RESTAR *ARGS ===")
    print(f"restar(20, 5, 3) = {restar(20, 5, 3)}") # 12
    print(f"restar() = {restar()}") # 0
    
    print("\n=== TEST 3: MULTIPLICAR *ARGS ===")
    print(f"multiplicar(2, 3, 4) = {multiplicar(2, 3, 4)}") # 24
    
    print("\n=== TEST 4: PROMEDIO *ARGS ===")
    print(f"promedio(4.5, 3.0, 5.0) = {promedio(4.5, 3.0, 5.0)}") # 4.17
    print(f"promedio vacío = {promedio()}") # 0
    
    print("\n=== TEST 5: **KWARGS API ===")
    registrar_api_endpoint(nombre="Sebas", rol="Backend Jr", pais="Colombia")