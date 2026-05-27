## # calculadora_v2.py - Día 3/180 | Hecho por: Sebas futuro Jr Mid ##

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    
def potencia(base, exponente):
        return base ** exponente    

def mostrar_menu():
    print("=== Calculadora PRO ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("6. Potencia")
print("==================================")

# AQUI EMPIEZA LA MAGIA: BUCLE INFINITO CONTROLADO #

while True:
    mostrar_menu()
    opcion = input("Elige una opcion 1-6: ")

    #ARMA 1: break - mata el bucle
    if opcion == "5":
        print("Gracias por usar la calculadora PRO. ¡Hasta luego!")
        break

    # Validamos opciones permitidas (¡Ajustada para que no falle con el 6!)
    opciones_validas = ["1", "2", "3", "4", "6"] # <-- AGREGA EL "6" AQUÍ EN TU RETO
    if opcion not in opciones_validas:
        print("❌ Opción inválida. Elige una opción del menú.")
        continue

    # ARMA 3: try/except - mata el ValueError que ocurre si el usuario mete algo que no es numero
    try:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
    except ValueError:
        print("Error: solo numeros, crack. intenta de nuevo.")
        continue # Vuelve al menu sin crashear

    if opcion == "1":
        print(f"\nresultado: {num1} + {num2} = {sumar(num1, num2)}")
    elif opcion == "2":
        print(f"\nresultado: {num1} - {num2} = {restar(num1, num2)}")
    elif opcion == "3":
        print(f"\nresultado: {num1} * {num2} = {multiplicar(num1, num2)}")
    elif opcion == "4":
        print(f"\nresultado: {num1} / {num2} = {dividir(num1, num2)}")
    elif opcion == "6":
        print(f"\nresultado: {num1} elevado a {num2} = {num1 ** num2}")

        input("\nPresiona Enter para volver al menu...")


    