# ============
# GESTOR DE TAREAS - DIA 13: PERSISTENCIA JSON
# Sebastian Botero - Dia 13-180
#=============

import json # <- Libreria estanda para guardar diccionarios 

#1 FUNCION PARA GUARDAR
def guardar_tareas():
    try:
        with open("tareas.json", "w", encoding="utf-8") as archivo:
         json.dump(tareas, archivo, indent=4, ensure_ascii=False) 
    except Exception as e:
        print(f"Error critico al gurdar los datos: {e}")

# 2. FUNCION PARA CARGAR

def cargar_tareas():
    try:
        with open("tareas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            tareas.clear()
            tareas.extend(datos)
    except FileNotFoundError:
        pass # Primera vez, no existe archivo. Normal.
    except json.JSONDecodeError:
        print("Archivo corrupto. Iniciando vacio.")

# 2. FLUJO PRINCIPAL
        
tareas = []
cargar_tareas()  #<- Carga lo guardado ayer

while True:
            print("\n--- MI GESTOR DE TAREAS PRO CON MEMORIA ---")
            print("1. Agregar tarea")
            print("2. Ver tareas")
            print("3. Marcar completada")
            print("4. Salir")
            
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
                    print("chao Sebas, Datos blindados en tareas json. Seguimos despues dia 14.")
                    break

            else:
             print("opcion invalida. Intenta de nuevo.")

        







