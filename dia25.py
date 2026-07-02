import json

# Constante global de cofiguracion centralizada
NOMBRE_ARCHIVO = "inventarios.json"

MESES_VALIDOS = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

#=============================
# 1. CLASE BASE
#=============================
class Producto:
    def __init__(self, nombre_articulo, precio_unitario, stock_cantidad, **Kwargs):
        """Inicializa las propiedades basicas de cualquier producto."""
        self.nombre = nombre_articulo
        self.precio = precio_unitario
        self.cantidad = stock_cantidad
        # Deja pasar los parameteos extras hacia la siguiente clase en el MRO (Method Resolution Order)
        super().__init__(**Kwargs)

    def calcular_subtotal(self):
        """Calcula el valor total del producto en stock."""
        return self.precio * self.cantidad
    
    def to_dict(self):
        """Serializa los datos base del producto."""
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "tipo": "generico"
        }
    
    def __str__(self):
        return f"{self.nombre} | Stock: {self.cantidad} | Subtotal: ${self.calcular_subtotal()}"
    
#=============================
# 2. CLASE HIJA 1 - PRODUCTO IMPORTADO
#=============================
class ProductoImportado(Producto):
    def __init__(self, impuesto_arancel, **kwargs):
        """Hijo de producto. Agrega logica de costos de importancion y blindaje"""
        #ARQUITECTURA DEFENSIVA: Validamos que el arancel sea un porcentaje logico
        if not (0 < impuesto_arancel <= 1):
            raise ValueError("El arancel debe ser un valor entre 0.01 y 1.0 (ej: 0.15 para 15%)")
        
        self.impuesto_arancel = impuesto_arancel
        # Deja pasar los parameteos extras hacia la siguiente clase en el MRO (Method Resolution Order)
        super().__init__(**kwargs)

    def calcular_subtotal(self):
        """Sobreescribe el calculo sumando el arancel de aduana."""
        costo_base = super().calcular_subtotal()
        return int(costo_base * (1 + self.impuesto_arancel))
    
    def to_dict(self):
        """Extiende la serializacion con los datos de importacion."""
        diccionario = super().to_dict()
        diccionario["impuesto_arancel"] = self.impuesto_arancel
        diccionario["tipo"] = "importado"
        return diccionario
    
    def __str__(self):
        texto_padre = super().__str__()
        return f"{texto_padre} | Arancel: {int(self.impuesto_arancel * 100)}%"
    
#=============================
# 3. CLASE HIJA 2 - PRODUCTO PERECEDERO
#=============================
class ProductoPerecedero(Producto):
    def __init__(self, mes_vencimiento, **kwargs):
        """Hijo de producto. Agrega control de fecha de vencimiento y blindaje"""
        if mes_vencimiento.lower() not in MESES_VALIDOS:
            raise ValueError(f"'{mes_vencimiento}' no es un mes válido.")
        
        self.mes_vencimiento = mes_vencimiento.capitalize()
        # Deja pasar los parameteos extras hacia la siguiente clase en el MRO (Method Resolution Order)
        super().__init__(**kwargs)

    def to_dict(self):
        """Extiende la serializacion con los datos de vencimiento."""
        diccionario = super().to_dict()
        diccionario["mes_vencimiento"] = self.mes_vencimiento
        diccionario["tipo"] = "perecedero"
        return diccionario

    def __str__(self):
        texto_padre = super().__str__()
        return f"{texto_padre} | Vence en: {self.mes_vencimiento}"
    
#=============================
#4. CLASE HIBRIDA -  HERENCIA MULTIPLE(NIVEL SENIOR)
#=============================
class ProductoImportadoPerecedero(ProductoImportado, ProductoPerecedero):
    def __init__(self, nombre_articulo, precio_unitario, stock_cantidad, impuesto_arancel, mes_vencimiento):
        """
        Clase hibrida con herencias multiple.
        Hereda de ProductoImportado y Prodcutoperecedero simultaneo.
        """
        # Aqui se empaquetan todos los argumentos con nombre explicito
        super().__init__(
            nombre_articulo=nombre_articulo,
            precio_unitario=precio_unitario,
            stock_cantidad=stock_cantidad,
            impuesto_arancel=impuesto_arancel,
            mes_vencimiento=mes_vencimiento
        )

    def to_dict(self):
        """Fusiona las serializaciones de ambos padres usando el MRO."""
        diccionario = super().to_dict()
        diccionario["tipo"] = "importado_perecedero"
        return diccionario
    
    def __str__(self):
        """Concatena las representaciones de toda la cadena jerarquica."""
        return super().__str__()
    
#=============================
# 5. PRUEBA DE CAMPO EN CONSOLA
#=============================
if __name__ == "__main__":
    print("___ DIAGNOSTICO DE ARQUITECTURA (DIA 25) ---\n")

    # 1. Producto hibrido completo
    # Queso parmesano: Traido de italia (15% arancel) y vence en octubre
    queso = ProductoImportadoPerecedero(
        nombre_articulo="Queso parmesano Reggiano",
        precio_unitario=85000,
        stock_cantidad=10,
        impuesto_arancel=0.15,
        mes_vencimiento="octubre"
    )
    print("Producto hibrido:")
    print(queso)
    print("\nDiccionario JSON resultante:")
    print(queso.to_dict())

    # 2. Inspeccion del MRO en vivo
    print("\n ORDEN DE RESOLUCION DE METODOS (MRO):")
    for i, clase in enumerate(ProductoImportadoPerecedero.__mro__, 1):
        print(f" paso {i}: {clase.__name__}")

    # 3. Pruebas de blindaje (Failing Fast)
    print("\n--- PRUEBAS DE BLINDAJE ---")
    try:
        malo = ProductoImportado(
            nombre_articulo="Celular",
            precio_unitario=1000,
            stock_cantidad=5,
            impuesto_arancel=1.5 #Arancel por las nubes (INVALIDO)
        )
    except ValueError as e:
        print(f" Arancel invalido capturado: {e}")

    try:
        malo2 = ProductoPerecedero(
            nombre_articulo="Yogur",
            precio_unitario=1000,
            stock_cantidad=5,
            mes_vencimiento="Martes" #Mes invalido (INVALIDO)
        )
    except ValueError as e:
        print(f" Mes invalido capturado: {e}")
