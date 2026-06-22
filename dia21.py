import json

#========================================================
# 1. EL MOLDE (CLASE) CON UN NUEVO METODO DE CONVERSACION
#========================================================
class Producto:
    def __init__(self, nombre_articulo, precio_unitario, stock_cantidad):
        self.nombre = nombre_articulo
        self.precio = precio_unitario
        self.cantidad = stock_cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad
    
    # NUEVO METODO PROFESIONAL: Convierte el objeto en un diccionario limpio
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }
    
    def __str__(self):
        return f"{self.nombre} | Stock: {self.cantidad} | Subtotal: ${self.calcular_subtotal()}"
    
    #=======================================================
    # 2. FLUJO PRINCIPAL (PEGADO A LA IZQUIERDA - COLUMNA 1)
    #=======================================================

    # PASO A: Creamos dos instancias reales en la memoria RAM (como el viernes)
prod_1 = Producto("Empanada de carne", 3000, 10)
prod_2 = Producto("Gaseosa 1.5L", 4500, 4)

# Paso B: Convertimos los objetos a diccionarios usando nuestro nuevo metodo
lista_productos_dict = [
    prod_1.to_dict(),
    prod_2.to_dict()
]

# Paso C: Guardar la lista de diccionarios dentro de un archivo JSON real
nombre_archivo = "inventarios.json"

print(" Guardando datos en el disco duro...")

#=================================================
# LEER DESDE DISCO Y RECONSTRUIR OBJETOS (LECTURA)
#=================================================
print("\n Leyendo datos desde el disco duro...")

try:
    # 1. Abrimos el archivo en modo lectura ("r")
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
       lista_leida = json.load(archivo)

    # 2. Creamos la lista donde guardaremos losobjetos reconstruidos
    producto_recuperados = []

    # 3. Elciclo for para pasar de diccionario a objetos reales
    for dato in lista_leida:
       producto = Producto(
           dato["nombre"],
           dato["precio"],
           dato["cantidad"]
       )
       producto_recuperados.append(producto)

# 4. Imprimimos los objetos usando el metodo magico __str__ 
    print("Productos recuperados y reconstruidos desde el archivo:")
    for p in producto_recuperados:
      print(p)

#====================================================
# 5. CONTROLADORES DE EXCEPCIONES (MANEJO DE ERRORES)
# ===================================================
# 
except FileNotFoundError:
    print(" Error: No se encontro el archivo inventarios.json.")
except json.JSONDecodeError:
    print("Error : El archivo JSON tiene un error de formato o esta corrupto.")

  
  
