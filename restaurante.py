import json
import os

# ==========================================
# 1. PERSISTENCIA DE DATOS (JSON)
# ==========================================

def guardar_pedidos(pedidos):
    """Guarda la lista de pedidos en el archivo JSON"""
    try:
        with open("pedidos.json", "w", encoding="utf-8") as archivo:
            json.dump(pedidos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f" Error crítico al guardar los datos: {e}")

def cargar_pedidos():
    """Carga los pedidos desde el archivo JSON al iniciar"""
    if os.path.exists('pedidos.json'):
        try:
            with open('pedidos.json', 'r', encoding='utf-8') as f:
                pedidos = json.load(f)
                print(f"[sistema] cargadas {len(pedidos)} tareas desde el archivo pedidos.json")
                return pedidos
        except Exception:
            print("[sistema] Archivo corrupto, iniciando lista vacía")
            return []
    else:
        print("[sistema] No hay archivo guardado, iniciando lista vacía")
        return []

# ==========================================
# 2. FUNCIONES DE LOGICAY CONTROL (CRUD)
# ==========================================

def pedir_datos_pedido():
    cliente = input(" Nombre del cliente: ").strip()
    plato = input(" Tipo de plato: ").strip()
    bebida = input(" Bebida: ").strip()
    
    # Combinamos la información para que se guarde en la clave 'texto' que ya lee tu código
    informacion_pedido = f"{cliente} -> Plato: {plato} | Bebida: {bebida}"
    
    return {
        "texto": informacion_pedido,
        "completada": False
    }

    

def completar_pedido():
    """Marca un pedido como completado por índice"""
    mostrar_pedidos_filtradas("todas")

    if not pedidos:
        return
     
    try:
        indice = int(input("Número de pedido a completar: ")) - 1
        if 0 <= indice < len(pedidos):
            pedidos[indice]["completada"] = True
            guardar_pedidos(pedidos)
            print(" Pedido marcado como despachado")
        else:
            print(" Índice inválido. Usa un número de la lista")
    except ValueError:
        print(" Error: Debes ingresar solo números")


# ==========================================
# 3. FILTROS E IMPRESIÓN INTELIGENTE (DÍA 19)
# ==========================================

def mostrar_pedidos_filtradas(filtro):
    """Filtra y muestra los pedidos usando List Comprehension de manera global"""
    if filtro == "pendientes":
        pedidos_filtradas = [t for t in pedidos if not t["completada"]]
        titulo = " PEDIDOS PENDIENTES"
    elif filtro == "completadas":
        pedidos_filtradas = [t for t in pedidos if t["completada"]]
        titulo = " PEDIDOS COMPLETADAS"
    else:
        pedidos_filtradas = pedidos
        titulo = "TODOS LOS PEDIDOS"
    
    print(f"\n--- {titulo} ---")
    if not pedidos_filtradas:
        print("No hay pedidos para mostrar en este filtro.")
        return
    # AQUÍ ESTÁ EL TRUCO: Usamos 'p' en singular para el ciclo
    for i, p in enumerate(pedidos_filtradas, 1):
        estado = "Despachado" if p["completada"] else "Pendiente"
        print(f"{i}. [{estado}] {p['texto']}")
    
    
      
        
        
# ==========================================
# 4. FLUJO PRINCIPAL Y MENÚ
# ==========================================
        
pedidos = cargar_pedidos()

def mostrar_menu():
    print("\n--- PEDIDOS RESTAURANTE ---")
    print("1. Agregar pedidos ")
    print("2. Ver todos los pedidos ")
    print("3. Marcar pedido como completado ")
    print("4. Ver solo pedidos pendientes ")
    print("5. Ver solo pedidos completadas ")
    print("6. Salir ")
    return input("Elige una opción: ")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nueva_pedido = pedir_datos_pedido()
        pedidos.append(nueva_pedido)
        guardar_pedidos(pedidos)
        print(" Guardada en disco con éxito.")

    elif opcion == "2":
        mostrar_pedidos_filtradas("todas")

    elif opcion == "3":
        completar_pedido()

     

    elif opcion == "4":
        mostrar_pedidos_filtradas("pendientes")

    elif opcion == "5":
        mostrar_pedidos_filtradas("completadas")

    elif opcion == "6":
        guardar_pedidos(pedidos)
        print("GRACIAS POR USAR EL SISTEMA, EXCELENTE DIA")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")