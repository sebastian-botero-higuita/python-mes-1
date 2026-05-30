import time
from functools import wraps

def medir_tiempo(func):
    """
    decorador: mide cuanto tarde una funcion en ejecutarse
    """
    @wraps(func)  #TORNILLO 2: preserva el nombre __name__ y docstring de la funcion original
    def wrapper(*args, **kwargs): #TORNILLO 1: acepta cualquier cantidad de argumentos
        print(f"\n[LOG] Ejecutando:'{func.__name__}'...")
        inicio = time.time()
        
        #TORNILLO 3: guardamos el resultado
        resultado = func(*args, **kwargs)

        fin = time.time()
        print(f"[LOG] '{func.__name__}' finalizo en {fin - inicio:.6f} segs.")

        #TORNILLO 4: devolvemos el resultado. sin esto tu funcion retorna None y eso puede romper cosas

        return resultado
    return wrapper

@medir_tiempo     # Azucar sintetica para: simular_procesamiento = medir_tiempo(simular_procesamiento)
def simular_procesamiento_banco(monto):
    time.sleep(0.5) # simulamos que el servidor tarde 0.5 seg
    return f"procesamiento de ${monto} completado con exito"

if __name__ == "__main__":
    respuesta = simular_procesamiento_banco(1500)
    print(f"Respuesta del sistema:{respuesta}")


def solo_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # BLINDADO: Buscamos "rol" solo en kwargs
        # Forzamos que las funciones que usen @solo_admin reciben rol omo keyword
        rol = kwargs.get("rol", None)

        if rol == "admin":
            # Permite paso y devuelve lo que la funcion retorne
            return func(*args, **kwargs)
        else:
            print("[ACCESO DENEGADO]: SE REQUIERE PERMISOS DE ADMINISTRADORES,")
            return None #bloquea el paso 
        
    return wrapper
@solo_admin
def eliminar_base_de_datos(**kwargs):
    return "Base de datos eiminada de forma segura"

if __name__ == "__main__":
    print("\n===PRUEBAS DE SEGURIDAD===")

    # PRUEBA 1: USUARIO NORMAL
    resultado1 = eliminar_base_de_datos(usuario="Sebas", rol="usuario")
    print(f"Resultado: {resultado1}") # Deberia permitir el paso

    # PRUEBA 2: USUARIO ADMIN
    resultado2 = eliminar_base_de_datos(usuario="Sebas", rol="admin")
    print(f"Resultado: {resultado2}") # Deberia bloquear el paso
