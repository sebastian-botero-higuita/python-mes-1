
class Producto:
    # El constructor ahora recibe terminos globales de la industria
    def __init__(self, nombre_articulo, precio_unitario, stock_cantidad):
        self.nombre = nombre_articulo
        self.precio = precio_unitario
        self.cantidad = stock_cantidad

    # Un metodo con un nombre estandar en sistema  de facturacion. 
    def calcular_subtotal(self):
        return self.precio * self.cantidad
    
    # El formateo limpio para los registros del sistema 
    def __str__(self):
        return f"[ARTICULO] {self.nombre} | Stock: {self.cantidad} | Subtotal: ${self.calcular_subtotal()}"
    
    #========================
    #FLUJO PRINCIPAL (PROBANDO EL SISTEMA GLOBAL)
    #========================

    # Ahora este mismo molde te sirve para el negocio de empanadas,
    # parauna tienda de tecnologias o para un supemercado.
producto_1= Producto("Empanadas de carne", 3000, 5)
producto_2 = Producto("Macbook Air M1", 4500000, 1)

print(producto_1)
print(producto_2)


