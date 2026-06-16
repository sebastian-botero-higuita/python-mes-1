# Empanadas

pedidos = [] 

while True: 
    print("1.Agregar pedido : ")
    print("2.Ver pedido del dia : ")
    print("3.Total de empanadas vendidas :")
    print("4.Buscar pedido por nombre: ")
    print("5.Eliminar pedido")
    print("6.Cerrar dia")

    opcion = input("Elige: ")

    if opcion == "1":
            nombre = input("pedido : ").strip().lower()
            cantidad = int(input("Cantidad: "))
            encontrado = False
            for pedido in pedidos:
                if pedido["nombre"] == nombre:  # Ya ambos están en minúscula
                 pedido["cantidad"] += cantidad  # Sumamos
                 encontrado = True
                 print(f"Pedido actualizado. {nombre} ahora tiene {pedido['cantidad']}")
                 break

            if not encontrado:
             pedidos.append({"nombre": nombre, "cantidad": cantidad})
             print(f"pedidos '{nombre}' agregado.")

   
    elif opcion == "2":
        if len(pedidos) == 0:
               print("No hay pedidos")
        else:
            print("--- TUS PEDIDOS ---")
            for i, pedido in enumerate(pedidos, 1):
             print(f"{i} {pedido['nombre']} {pedido['cantidad']} empanada (s)")

    elif opcion == "3":
         total = 0
         for pedido in pedidos:
              total = total + pedido["cantidad"]
         print(f" Total vendidas : {total} empanadas")

    elif opcion == "4":
        nombre_buscar = input("Nombre del cliente a buscar ? ").strip().lower()
        encontrado = False

        for pedido in pedidos:
            #comparamos pasando el nombre guardado a minuscula
            if pedido["nombre"].lower() == nombre_buscar:
                print(f"pedido encontrado: {pedido['nombre']} lleva {pedido['cantidad']} empanadas.")
                encontrado = True

        if not encontrado: # si la bandera quedo en false, el cliente no existe
            print("Ese cliente no tiene pedido registrado hoy.")

    elif opcion == "5":
       nombre_eliminar = input("Nombre del cliente que cancelo ? ").strip().lower()
       encontrado = False

       for pedido in pedidos:
           if pedido["nombre"].lower() == nombre_eliminar:
               pedidos.remove(pedido)  #Borra el pedido completo de la lista
               print(f"El pedido de '{pedido['nombre']}'Fue eliminado con exito.")
               encontrado = True
               break #OBLIGATORIO
           
       if not encontrado:
               print("No se encontro ningun pedido con ese nombre.")

    elif opcion == "6":    
        print("Dia cerrado. ! Gracias por usar el sistema!")
        break                    





