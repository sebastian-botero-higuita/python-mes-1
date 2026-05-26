print("=== Calculadora Dia 2/180 ===")

num1 = float(input("Ingresa el primer numero:"))
num2 = float(input("ingresa el segundo numero:"))
operaciones = input("elige +, -, *, / :")

if operaciones == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operaciones == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operaciones == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operaciones == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida. Por favor, elige entre +, -, *, /.")
    
  