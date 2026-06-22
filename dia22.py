
import json

#========================
# 1. LA CLASE PRODUCTO
#========================
class Producto:
    def __init__(self, nombre_articulo, precio_unitario, stock_cantidad):
        self.nombre = nombre_articulo
        self.precio = precio_unitario
        self.cantidad = stock_cantidad

    def calcular_subtotal(self):
        """Calcular el valor total del producto en stock."""
        return self.precio * self.cantidad
    
    def to_dict(self):
        """Convierte el objeto en diccionario para persistencia JSON."""
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }
    def __str__(self):
        return f"{self.nombre} | Stock: {self.cantidad} | Subtotal: ${self.calcular_subtotal()}"
    
#==============================
# 2. FUNCIONES DEL MENU
#==============================

def mostrar_menu():
    """Muestra las opciones del menu pricipalen la terminal."""
    print("\n" + "="*30)
    print(" SISTEMA DE INVENTARIO")
    print("="*30)
    print("1. Agregar nuevo producto")
    print("2. Ver inventario actual")
    print("3. Guardar y Salir")
    print("="*30)

def agregar_producto(inventario):
    """Solicita datos al usario y agrega un nuevo producto al inventario."""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Nombre del articulo: ").strip()

    # Validacion de texto vacio
    if not nombre:
        print(" El nombre no puede estar vacio.")
        return
    
    # Blindaje contra letras en campos numericos
    try:
        precio = int(input("Precio unitario: "))
        cantidad = int(input("Cantidad en stock: "))

        if precio <= 0 or cantidad <=0:
           print(" El precio y la cantidad deben ser mayores a cero.")
           return

    except ValueError:
        print(" Error: el precio y la cantidad deben ser números enteros.")
        return

 # Si pasa todas las pruebas, se crea el objeto y se mete a la lista
    nuevo_producto = Producto(nombre, precio, cantidad)
    inventario.append(nuevo_producto)
    print(f"¡{nombre} agregado exitosamente!")

def ver_inventario(inventario):
    """Muestra todos los productos del inventario en memoria."""
    print("\n--- INVENTARIO ACTUAL EN MEMORIA ---")
    if not inventario:
        print("El inventario esta vacio. ¡Agrega un producto primero!")
        return
    for item in inventario:
        print(item)

def guardar_y_salir(inventario):
    """Guarda el inventario en disco y termina el programa."""
    try:
        with open("inventarios.json", "w", encoding="utf-8") as archivo:
            # Usamos una lista de comprension para serializar cada objeto antes de guardarlo
            json.dump([p.to_dict() for p in inventario], archivo, indent=4, ensure_ascii=False)
        print(" Inventario guardado exitosamente en inventarios.json")
    except IOError as e:
        print(f" Error al guardar el archivo: {e}")

#=================================
# 3. LOOP PRINCIPAL (EVENT LOOP)
#=================================
inventario_activo = []

while True:
    mostrar_menu()
    opcion = input(" Selecciona una opcion (1-3): ").strip()

    if opcion == "1":
        agregar_producto(inventario_activo)
    elif opcion == "2":
        ver_inventario(inventario_activo)
    elif opcion == "3":
        guardar_y_salir(inventario_activo)
        print(" ¡Gracias por usar el sistema, Sebas! Programa cerrado de forma limpia.")
        break # Rompe el ciclo infinito y apaga el script
    else:
        print(" Opcion invalida. Por favor, digite un numero entre 1 y 3.")




    