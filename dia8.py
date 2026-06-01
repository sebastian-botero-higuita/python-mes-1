import sys

def lista_cuadrados(n):
    resultado = []
    for i in range(n):
        resultado.append(i**2)
    return resultado

def generador_cuadrados(n):
    for i in range(n):
        yield i**2

def generador_infinito():
    numero = 1
    while True:
        yield numero
        numero += 2     

if __name__ == "__main__":
    numeros_lista = lista_cuadrados(1000000)
    peso_lista =sys.getsizeof(numeros_lista) / (1024 * 1024)
    print(f" Lista completa : {peso_lista:.2f} MB")
    print("\n=== PRUEBA stopIteration ===")
    gen_pequeno = generador_cuadrados(2) # solo tiene 2 elementos: 0 y 1
    print(f"Elemento 1: {next(gen_pequeno)}")
    print(f"Elemento 2: {next(gen_pequeno)}")
   
try:
        print(f"Elemento 3: {next(gen_pequeno)}")
except StopIteration:
    print("StopIteration atrapada: El generador se quedo sin datos")
    
    print("\n=== PRUEBA INFINITO CONTROLADO ===")
    impares = generador_infinito()

    print(next(impares)) # 1
    print(next(impares)) # 3
    print(next(impares)) # 5
    print(next(impares)) # 7
    print("... y paramos antes de que la mac llore")

    objeto_generador = generador_cuadrados(1000000)
    peso_gen = sys.getsizeof(objeto_generador)
    print(f" Generador: {peso_gen} bytes. Misma info, 0 RAM")

    #TORNILLO DE ENTREVISTA: next()
    print(f"Primer elemento: {next(objeto_generador)}")
    print(f"Segundo elemento: {next(objeto_generador)}")


