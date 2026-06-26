import json

# Constante global: un solo lugar para controlar el nombre del archivo 
NOMBRE_ARCHIVO = "inventario.json"

MESES_VALIDOS = [
    "enero", "febrero", "marzo,", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

#=================================
# 1. CLASE PADRE (BASE)
#=================================
class Producto:
    def __init__(self, nombre_articulo, precio_unitario, stock_cantidad):
        """Inicializa un producto con nombre, precio y cantidad en stock."""
        self.nombre = nombre_articulo
        self.precio = precio_unitario
        self.cantidad = stock_cantidad

    def calcular_subtotal(self):
        """Calcula el valor total del producto en stock."""
        return self.precio * self.cantidad
    
    def to_dict(self):
        """Convierte el objeto en diccionario para persistencia JSON."""
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "tipo": "generico"
        }
    def __str__(self):
        return f"{self.nombre} | Stock: {self.cantidad} | Subtotal: ${self.calcular_subtotal()}"
    
    # =====================================================================
# 2. CLASE HIJA (HERENCIA + SUPER())
# =====================================================================
class ProductoPerecedero(Producto):
    def __init__(self, nombre_articulo, precio_unitario, stock_cantidad, mes_vencimiento):
        """
        Inicializa un producto perecedero heredando del Producto base.
        
        El padre maneja nombre, precio y cantidad.
        El hijo agrega el mes de vencimiento como atributo especial.
        """
        # super() llama al constructor del padre para no repetir su lógica
        super().__init__(nombre_articulo, precio_unitario, stock_cantidad)
        
        # ARQUITECTURA DEFENSIVA: Validamos que el mes sea real antes de asignarlo
        if mes_vencimiento.lower() not in MESES_VALIDOS:
            raise ValueError(f"'{mes_vencimiento}' no es un mes válido.")
            
        self.mes_vencimiento = mes_vencimiento.capitalize()

    def __str__(self):
        """Extiende el __str__ del padre agregando el mes de vencimiento."""
        # super().__str__() trae "📦 Nombre | Stock: X | Subtotal: $Y"
        texto_padre = super().__str__()
        return f"{texto_padre} | ⚠️ Vence en: {self.mes_vencimiento}"

    def to_dict(self):
        """Extiende el to_dict del padre agregando el mes de vencimiento."""
        # Traemos el diccionario base del padre y le agregamos lo nuestro
        diccionario = super().to_dict()
        diccionario["mes_vencimiento"] = self.mes_vencimiento
        diccionario["tipo"] = "perecedero"
        return diccionario
    
    # =====================================================================
# 3. PRUEBA DE CAMPO EN CONSOLA
# =====================================================================
if __name__ == "__main__":
    print("--- 🧪 PROBANDO HERENCIA Y SUPER() ---\n")

    # 1. Producto normal (Padre)
    articulo_normal = Producto("Tennis", 450000, 12)
    print(articulo_normal)

    # 2. Producto perecedero (Hijo) con mes válido
    articulo_comida = ProductoPerecedero("Leche Entera", 4500, 50, "Julio")
    print(articulo_comida)

    # 3. El hijo usa calcular_subtotal() del padre sin haberlo redefinido
    print(f"\nSubtotal de la leche: ${articulo_comida.calcular_subtotal()}")

    # 4. Serialización para JSON
    print("\nFormatos JSON resultantes:")
    print("Padre:", articulo_normal.to_dict())
    print("Hijo :", articulo_comida.to_dict())

    # 5. Prueba de validación de arquitectura — mes inválido
    print("\n--- 🧪 PRUEBA DE MES INVÁLIDO ---")
    try:
        producto_mal = ProductoPerecedero("Yogur", 3000, 20, "Martes")
    except ValueError as e:
        print(f"✅ Error capturado correctamente: {e}")
        
     