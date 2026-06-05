# ======= PARTE 1: ENTENDER LISTAS =======

print("=== PARTE 1: ENTENDER LISTAS ===")
tareas = ["Estudiar python", "Subir a GitHub", " Dormir tranquilo"]

print(tareas)
print(tareas[0])
print(tareas[-1])
print(len(tareas))

print("=== PARTE 2: 7 METODOS CLAVE ===")
tareas = []

tareas.append("aprender listas")
print(f"Después de append: {tareas}")

tareas.insert(0, "Abrir VS code")
print(f"Después de insert: {tareas}")

tareas.remove("Abrir VS code")
print(f"Después de remove: {tareas}")

ultima = tareas.pop()
print(f"Saque: {ultima} | Listas ahora: {tareas}")

print(f"Total tareas: {len(tareas)}")
print(f"¿'Aprender listas' esta? {'aprender listas' in tareas}")

tareas.append("Subir a Github")
tareas.append("Descansar")
for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea}")

    ## === PARTE 3: PROYECTO REAL ====
    print("\n=== PARTE 3: GESTOR DE TAREAS DIA 11 ===")
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea 2. Ver tareas 3. Completar tarea 4. Salir")
        opcion = input("Elige: ")

        if opcion == "1":
            tarea = input(" Que tarea agregaras?")
            lista_tareas.append(tarea)
            print(f"Tarea '{tarea}' agregada.")

        elif opcion == "2":
            if len(lista_tareas) == 0:
               print("No hay tareas pendientes")
            else:
               print("n--- TUS TAREAS ---")
            for i, tarea in enumerate(lista_tareas, 1):
                   print(f"{i}. {tarea}")

        elif opcion == "3":
            if len(lista_tareas) == 0:
               print("No hay tareas para completar")
            else:
             num = int(input("Numero de tarea a completar: "))
             tarea_completada = lista_tareas.pop(num - 1)
             print(f"Tarea completada: {tarea_completada}")
        elif opcion == "4":
                print(" Nos vemos mañana dia 12. Buen trabajo! ")
                break

        else:
          print("Opcion invalida. Usa 1, 2, 3 o 4.")
