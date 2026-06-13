# ============
# GESTOR DE TAREAS - DIA 13: PERSISTENCIA JSON
# Sebastian Botero - Dia 13-180
#=============
import json
import os

# ==========================================
# 1. PERSISTENCIA DE DATOS (JSON)
# ==========================================

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON"""
    try:
        with open("tareas.json", "w", encoding="utf-8") as archivo:
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f" Error crítico al guardar los datos: {e}")

def cargar_tareas():
    """Carga las tareas desde el archivo JSON al iniciar"""
    if os.path.exists('tareas.json'):
        try:
            with open('tareas.json', 'r', encoding='utf-8') as f:
                tareas = json.load(f)
                print(f"[sistema] cargadas {len(tareas)} tareas desde el archivo tareas.json")
                return tareas
        except Exception:
            print("[sistema] Archivo corrupto, iniciando lista vacía")
            return []
    else:
        print("[sistema] No hay archivo guardado, iniciando lista vacía")
        return []

# ==========================================
# 2. FUNCIONES DE LOGICAY CONTROL (CRUD)
# ==========================================

def pedir_datos_tarea():
    """Pide los datos en la terminal para crear el diccionario de la tarea"""
    texto = input("Escribe la tarea: ").strip()
    prioridad = input("Prioridad (Alta/Media/Baja): ").strip().lower()
    
    # Validación por si el usuario presiona enter sin escribir la prioridad
    if prioridad not in ["alta", "media", "baja"]:
        prioridad = "media" # Por defecto
        
    return {
        "texto": texto,
        "completada": False,
        "prioridad": prioridad
    }

def completar_tarea():
    """Marca una tarea como completada por índice"""
    mostrar_tareas_filtradas("todas")

    if not tareas:
        return
     
    try:
        indice = int(input("Número de tarea a completar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            guardar_tareas(tareas)
            print(" Tarea marcada como completa")
        else:
            print(" Índice inválido. Usa un número de la lista")
    except ValueError:
        print(" Error: Debes ingresar solo números")

def editar_tarea():
    """Modifica el texto de una tarea existente sin alterar su estado o prioridad"""
    mostrar_tareas_filtradas("todas")

    if not tareas:
        return
     
    try:
        indice = int(input("Número de tarea a editar: ")) - 1
        if 0 <= indice < len(tareas):
            nuevo_texto = input("Escribe el nuevo texto para la tarea: ").strip()

            if nuevo_texto:
                tareas[indice]["texto"] = nuevo_texto
                guardar_tareas(tareas)
                print("Tarea actualizada con éxito.")
            else:
                print(" El texto no puede estar vacío. No se modificó nada.")
        else:
            print(" Índice inválido. Usa un número de la lista.")
    except ValueError:
        print(" Error: Debes ingresar solo números enteros.")

def eliminar_tarea():
    """Elimina una tarea por completo de la lista y del disco duro"""
    mostrar_tareas_filtradas("todas")

    if not tareas:
        return 
     
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1

        if 0 <= indice < len(tareas):
            tarea_borrada = tareas.pop(indice)
            guardar_tareas(tareas)
            print(f" Tarea '{tarea_borrada['texto']}' eliminada con éxito.")
        else:
            print(" Índice inválido. Usa un número de la lista.")
    except ValueError:
        print(" Error: Debes ingresar solo números enteros.")

# ==========================================
# 3. FILTROS E IMPRESIÓN INTELIGENTE (DÍA 19)
# ==========================================

def mostrar_tareas_filtradas(filtro):
    """Filtra y muestra las tareas usando List Comprehension de manera global"""
    if filtro == "pendientes":
        tareas_filtradas = [t for t in tareas if not t["completada"]]
        titulo = " TAREAS PENDIENTES"
    elif filtro == "completadas":
        tareas_filtradas = [t for t in tareas if t["completada"]]
        titulo = " TAREAS COMPLETADAS"
    else:
        tareas_filtradas = tareas
        titulo = "📋 TODAS LAS TAREAS"
    
    print(f"\n--- {titulo} ---")
    if not tareas_filtradas:
        print("No hay tareas para mostrar en este filtro.")
        return
    
    for i, tarea in enumerate(tareas_filtradas, 1):
        estado = "Hecho" if tarea["completada"] else "Pendiente"
        prioridad = tarea.get("prioridad", "media")
        
        # Asignamos el emoji según la prioridad que guardaste
        emoji_prio = " alta" if prioridad == "alta" else "media" if prioridad == "media" else " baja"
        
        print(f"{i}. [{estado}] {tarea['texto']} - Prio: {emoji_prio}")

# ==========================================
# 4. FLUJO PRINCIPAL Y MENÚ
# ==========================================
        
tareas = cargar_tareas()

def mostrar_menu():
    print("\n--- MI GESTOR DE TAREAS PRO V2.5 ---")
    print("1. Agregar tarea ")
    print("2. Ver todas las tareas ")
    print("3. Marcar tarea como completada ")
    print("4. Editar texto de una tarea ")
    print("5. Eliminar una tarea ")
    print("6. Ver solo tareas pendientes ")
    print("7. Ver solo tareas completadas ")
    print("8. Salir ")
    return input("Elige una opción: ")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nueva_tarea = pedir_datos_tarea()
        tareas.append(nueva_tarea)
        guardar_tareas(tareas)
        print(" Guardada en disco con éxito.")

    elif opcion == "2":
        mostrar_tareas_filtradas("todas")

    elif opcion == "3":
        completar_tarea()
     
    elif opcion == "4":
        editar_tarea()

    elif opcion == "5":
        eliminar_tarea()

    elif opcion == "6":
        mostrar_tareas_filtradas("pendientes")

    elif opcion == "7":
        mostrar_tareas_filtradas("completadas")

    elif opcion == "8":
        guardar_tareas(tareas)
        print("¡Chao Sebas! Datos blindados en tareas.json. ¡Día 19 coronado!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")





