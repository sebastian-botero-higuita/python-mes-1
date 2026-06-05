# ============
# GESTOR DE TAREAS - DIA 12: DICCIONARIOS
# Sebastian Botero - Dia 12/180
#=============

# Lista que guarda diccionario en vez de solo texto
tareas = []

#MENU PRINCIPAL
while True:
    print("\n--- MI GESTOR DE TAREAS PRO ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

    opcion = input("Elige una opcion ")

    # OPCION 1: AGREGAR TAREA COMO DICCIONARIO
    if opcion == "1":
        texto = input("Escribe la tarea: ")
        prioridad = input("Prioridad (Alta, Media, Baja): ")

        # AQUI ESTA LA MAGIA: creamos diccionario con texto y prioridad
        nueva_tarea = {
            "texto": texto,
            "completada": False,
            "prioridad": prioridad
        }
        tareas.append(nueva_tarea)
        print("Tarea agregada con exito!")

        #OPCION 2: VER TAREAS
    elif opcion == "2":
        if len(tareas) == 0:
            print("No tienes tareas todavia")
        else:
            print("\nTUS TAREAS:")
            for i, tarea in enumerate(tareas):
                estado = "Hecha" if tarea["completada"] else "Pendiente"
                print(f"{i+1}.[{estado}] {tarea['texto']} - prioridad: {tarea['prioridad']}")

                # OPCION 3: MARCAR COMPLETADA
    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para completar")
        else:
            indice = int(input("Numero de tarea a completar: ")) - 1
            tareas[indice]["completada"] = True
            print("Tarea marcada como completada")

            #OPCION 4:SALIR
    elif opcion == "4":
        print("Chao Sebastian, nos vemos mañana para el dia 13! Buen trabajo!")
        break

    else:
        print("Opcion invalida. Intenta de nuevo.")







