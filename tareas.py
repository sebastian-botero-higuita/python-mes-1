# ============
# GESTOR DE TAREAS - DIA 13: PERSISTENCIA JSON
# Sebastian Botero - Dia 13-180
#=============

import json # <- Libreria estanda para guardar diccionarios 
import os 

#1 FUNCION PARA GUARDAR
def guardar_tareas():
    try:
        with open("tareas.json", "w", encoding="utf-8") as archivo:
         json.dump(tareas, archivo, indent=4, ensure_ascii=False) 
    except Exception as e:
        print(f"Error critico al gurdar los datos: {e}")

def cargar_tareas():
    global tareas
    if os.path.exists('tareas.json'):
        with open('tareas.json', 'r', encoding='utf-8') as f:
            tareas = json.load(f)
            print(f"[sistema] cargadas {len(tareas)} tareas desde el archivo tareas.json")


# 2. FUNCION PARA CARGAR

def editar_tarea():
    if len(tareas) == 0:
        print("No tienes tareas todavía para editar.")
        return

    try:
        indice = int(input("Número de tarea a editar: ")) - 1
        if 0 <= indice < len(tareas):
            nuevo_texto = input(f"Nuevo texto para '{tareas[indice]['texto']}': ")
            tareas[indice]['texto'] = nuevo_texto
            guardar_tareas() # Sincroniza con tu tareas.json inmediato
            print(" Tarea editada con éxito")
        else:
            print(" Número inválido. Esa tarea no existe.")
    except ValueError:
        print(" Error: Escribe solo números enteros.")

def eliminar_tarea():
    if len(tareas) == 0:
        print(" No tienes tareas todavía para eliminar.")
        return
    
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_borrada = tareas.pop(indice)
            guardar_tareas() # Sincroniza la eliminación en tu tareas.json
            print(f" Eliminada con éxito: '{tarea_borrada['texto']}'")
        else:
            print(" Número inválido. Esa tarea no existe.")
    except ValueError:
        print(" Error: Escribe solo números enteros.")

# 3. FLUJO PRINCIPAL
        
tareas = []
cargar_tareas()  #<- Carga lo guardado ayer

while True:
            print("\n--- MI GESTOR DE TAREAS PRO CON MEMORIA ---")
            print("1. Agregar tarea")
            print("2. Ver tareas")
            print("3. Marcar completada")
            print("4. Editar tarea")
            print("5. Eliminar tarea")
            print("6. Salir")
            
            opcion = input("Elige: ")

            if opcion == "1":
                texto = input("Tarea: ")
                prioridad = input("Prioridad Alta/Media/Baja: ")
                nueva_tarea = {"texto": texto, "completada": False, "prioridad": prioridad}
                tareas.append(nueva_tarea)
                guardar_tareas()  # <- GUARDA YA 
                print("Guardada en disco ")

            elif opcion == "2":
                if len(tareas) == 0:
                    print("Sin tareas aun.")
                else:
                    for i, t in enumerate(tareas):
                        estado=" Hecha" if t["completada"] else "pendiente"
                        print(f"{i+1}. [{estado}] {t['texto']} - {t['prioridad']}")

            elif opcion == "3":
                if len(tareas) == 0:
                    print("No hay tareas.")
                else:
                    try:
                        indice = int(input("Numero: ")) - 1
                        if 0 <= indice < len(tareas):
                            tareas[indice]["completada"] = True
                            guardar_tareas()   # <- GUARDAMOS EL CAMBIO DE ESTADO INSTANTANEAMENTE
                            print("Tarea marcada como completada y guardada en disco")
                        else:
                            print("Numero de tarea invalido.")
                    except ValueError:
                        print(" Por favor, ingrese un numero valido.")

            elif opcion == "4":
                editar_tarea()

            elif opcion == "5":
                eliminar_tarea()

            elif opcion == "6":
                    guardar_tareas()
                    print("chao Sebas, Datos blindados en tareas json. Seguimos despues dia 14.")
                    break

            else:
             print("opcion invalida. Intenta de nuevo.")

        







