## dia4.py - Calculadora v3 con history | Dia 4/180 | Hecho por: Sebas futuro Jr Mid ##

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b
def potencia(a, b): return a ** b

historial = [] # Lista para guardar el historial de operaciones

while True:
    print("\n=== CALCULADORA V3 CON HISTORY ===")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. potencia")
    print("6. show history")
    print("7. salir")

    print("==================================")

    opcion = input("Elige una opción (1-7): ")
    
    if opcion == "7":
        print("Thanks for using the calc. Bye!")
        break
    
    if opcion == "6":
        print("\n=== HISTORY ===")
        if len(historial) == 0:
            print("History is empty")
        else:
            for i, item in enumerate(historial, 1):
                print(f"{i}. {item}")
        input("\nPresiona Enter to continue...")
        continue
        
    if opcion not in ["1", "2", "3", "4", "5"]:
        print("Opción inválida. Elige entre 1-7.")
        continue
    
    try:
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
    except ValueError:
        print("Error: Solo se permiten números.")
        continue
    
    if opcion == "1":
        res = sumar(num1, num2)
        linea = f"{num1} + {num2} = {res}"
        print(f"\nResultado: {res}")
        historial.append(linea)
        
    elif opcion == "2":
        res = restar(num1, num2)
        linea = f"{num1} - {num2} = {res}"
        print(f"\nResultado: {res}")
        historial.append(linea)
        
    elif opcion == "3":
        res = multiplicar(num1, num2)
        linea = f"{num1} * {num2} = {res}"
        print(f"\nResultado: {res}")
        historial.append(linea)
        
    elif opcion == "4":
        if num2 == 0:
            linea = f"{num1} / {num2} = Error: División por cero"
            print("\nError: No se puede dividir por cero.")
            historial.append(linea)
        else:
            res = dividir(num1, num2)
            linea = f"{num1} / {num2} = {res}"
            print(f"\nResultado: {res}")
            historial.append(linea)
        
    elif opcion == "5":
        res = potencia(num1, num2)
        linea = f"{num1} ** {num2} = {res}"
        print(f"\nResultado: {res}")
        historial.append(linea)
    
    input("\nPresiona Enter to continue...")
