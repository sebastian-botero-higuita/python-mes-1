# dia5.py - Calculadora V4: Dispatch Table + Dict Historial | Día 5/180
# Hecho por: Sebas futuro Jr Mid

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b): return a ** b

# Tabla de despacho (Dispatch Table)
operaciones = {
    "1": sumar,
    "2": restar,
    "3": multiplicar,
    "4": dividir,
    "5": potencia
}

historial = []

print("=== CALCULADORA V4: DISPATCH TABLE + DICTS ===")

while True:
    print("\n1.Sumar | 2.Restar | 3.Multiplicar | 4.Dividir | 5.Potencia | 6.Show History | 7.Salir")
    op = input("Elige una opción (1-7): ") 
    if op == "7":
        print("Chao Sebas. Día 5 completado. ")
        break

    if op == "6":
        print("\n=== HISTORY (DATOS ESTRUCTURADOS) ===")
        if not historial:
            print("History is empty")
        else:
            for i, reg in enumerate(historial, 1):
                if reg["status"] == "ok":
                    print(f"{i}. [{reg['operacion'].upper()}] -> {reg['num1']} {reg['simbolo']} {reg['num2']} = {reg['resultado']}")
                else:
                    print(f"{i}.  Intento fallido en [{reg['operacion']}]: {reg['resultado']}")
        input("\nPresiona Enter para continuar...")
        continue

    if op not in operaciones:
        print(" Opción inválida. Usa del 1 al 7.")
        continue

    try:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
    except ValueError:
        print(" Error: Solo se permiten números.")
        continue

    funcion_matematica = operaciones[op]
    resultado = funcion_matematica(n1, n2)

    simbolos = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "**"}

    status_operacion = "error" if str(resultado).startswith("Error") else "ok"

    registro = {
        "operacion": funcion_matematica.__name__,
        "num1": n1,
        "num2": n2,
        "simbolo": simbolos[op],
        "resultado": resultado,
        "status": status_operacion
    }

    historial.append(registro)

    if status_operacion == "ok":
        print(f"Resultado: {resultado}")
    else:
        print(f" {resultado}")

    input("\nPresiona Enter para continuar...")