# ============
# GESTOR DE TAREAS - DIA 13: PERSISTENCIA JSON
# Sebastian Botero - Dia 13-180
#=============

import json # <- Libreria estanda para guardar diccionarios 
import os 

#1 FUNCION PARA GUARDAR
def guardar_tareas(tareas):
    import json
    try:
        with open("tareas.json", "w", encoding="utf-8") as archivo:
         json.dump(tareas, archivo, indent=4, ensure_ascii=False) 
    except Exception as e:
        print(f"Error critico al gurdar los datos: {e}")

def cargar_tareas():
    import os
    import json

    if os.path.exists('tareas.json'):
     try:
        with open('tareas.json', 'r', encoding='utf-8') as f:
            tareas = json.load(f)
            print(f"[sistema] cargadas {len(tareas)} tareas desde el archivo tareas.json")
            return tareas
     except:
          print("[sistema] Archivo corrupto, iniciando lista vacia")
          return[]
     else:
         print("[sistema] No hay archivo guardado, iniciando lista vacia")
         return []


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
            guardar_tareas(tareas) # Sincroniza la eliminación en tu tareas.json
            print(f" Eliminada con éxito: '{tarea_borrada['texto']}'")
        else:
            print(" Número inválido. Esa tarea no existe.")
    except ValueError:
        print(" Error: Escribe solo números enteros.")

# 3. FLUJO PRINCIPAL
        
tareas = cargar_tareas()  #<- Carga lo guardado ayer

def mostrar_menu():
    print("\n--- MI GESTOR DE TAREAS PRO V2.0 ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Editar texto de una tarea")
    print("5. Eliminar una tarea")
    print("6. Salir ")
    return input("Elige una opcion: ")

def pedir_datos_tarea():
    texto = input("Escribe la tarea: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    return {
        "texto": texto,
        "completada": False,
        "prioridad": prioridad,
    }

def mostrar_tareas():
     """Muestra todas las tareas guardadas en la lista con su estado"""
     if not tareas:
          print("No hay tareas pendientes")
          return
     for i, tarea in enumerate(tareas, 1):
          estado = "X" if tarea["completada"] else "Pendiente"
          print(f"{i}. [{estado}] {tarea['texto']} - {tarea['prioridad']}")



def completar_tarea():
     """Marca una tarea como completada por indice"""
     mostrar_tareas()

     if not tareas:
          print("No hay tareas para completar")
          return
     
     try:
          indice = int(input("Numero de tarea a completar: ")) -1
          if 0 <= indice < len(tareas):
               tareas[indice]["completada"] = True
               guardar_tareas(tareas)
               print("Tarea marcada como completa")

          else :
               print("Indice invalido. Usa un numero de la lista")
     except ValueError:
          print("Error: Debes ingresar solo numeros")

def eliminar_tareas():
    """Elimina una tarea por completo de la lista y del disco duro"""
    mostrar_tareas()

    if not tareas:
         return # Si no hay tareas, mostar_tareas ya aviso, asi que nos salimos 
     
    try:
         indice = int(input("Numero de tarea a eliminar:")) -1

         if 0 <= indice < len(tareas):
              print(f"tarea '{tarea_borrada['texto']}' eliminada con exito.")
         else:
              print("indice invalido. Usa un numero de lalista.")
    except ValueError:
         print("Error: Debes ingresar solo numeros enteros.")

def editar_tarea():
     """Modifica el texto de una tarea existente sin alterar su estado o prioridad"""
     mostrar_tareas()

     if not tareas:
          return
     
     try:
         indice = int(input("Numero de tarea a editar: ")) -1
         if 0 <= indice < len(tareas):
              nuevo_texto = input("Escribe el nuevo texto para la tarea: ").strip()

              if nuevo_texto: # Validamos que el usuario no mande un texto vacio
                   tareas[indice]["texto"] = nuevo_texto
                   guardar_tareas(tareas) #Guardamos el cambio en el JSON
                   print("Tarea actualizada con exito.")
              else:
                   print("El texto no puede estar vacio. No se modifico nada.")
         else:
              print("indice invalido. Usa un numero de la lista.")
     except ValueError:
      print("Error: Debes ingresar solo numeros enteros.")

     
         




while True:
       opcion = mostrar_menu()

       if opcion == "1":
                nueva_tarea = pedir_datos_tarea()
                tareas.append(nueva_tarea)
                guardar_tareas(tareas)  # <- GUARDA YA 
                print("Guardada en disco ")

       elif opcion == "2":
                if len(tareas) == 0:
                    print("Sin tareas aun.")
                else:
                    for i, t in enumerate(tareas):
                        estado=" Hecha" if t["completada"] else "pendiente"
                        print(f"{i+1}. [{estado}] {t['texto']} - {t['prioridad']}")

       elif opcion == "3":
            completar_tarea()
     

       elif opcion == "4":
                editar_tarea()

       elif opcion == "5":
                eliminar_tarea()

       elif opcion == "6":
                    guardar_tareas(tareas)
                    print("chao Sebas, Datos blindados en tareas json. Seguimos despues dia 14.")
                    break

       else:
             print("opcion invalida. Intenta de nuevo.")

        







