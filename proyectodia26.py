
import json

NOMBRE_ARCHIVO = "empleados.json"

# ===========================
# 1. CLASE BASE EMPLEADO
# ===========================
class Empleado:
    def __init__(self, nombre_empleado, salario_base, departamento_empleado):
        """Inicializa las propiedades basicas del empleado."""
        self.nombre = nombre_empleado
        self.salario = salario_base
        self.departamento = departamento_empleado

        if self.salario < 0:
            raise ValueError("El salario debe ser mayor a 0.")

    def calcular_pago(self):
        """Calcula el pago base del empleado."""
        return self.salario

    def to_dict(self):
        """Serializa los datos del empleado."""
        return {
            "nombre": self.nombre,
            "salario": self.salario,
            "departamento": self.departamento,
            "tipo": "planta"
        }

    def __str__(self):
        return f"{self.nombre} | Departamento: {self.departamento} | Salario: ${self.salario}"


# ===========================
# 2. CLASE HIJA CONTRATISTA
# ===========================
class EmpleadoContratista(Empleado):
    def __init__(self, nombre_empleado, salario_base, departamento_empleado,
                 horas_trabajadas, valor_hora):
        """Inicializa las propiedades del empleado contratista."""
        super().__init__(nombre_empleado, salario_base, departamento_empleado)
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

        if self.horas_trabajadas <= 0 or self.valor_hora <= 0:
            raise ValueError("Las horas y el valor por hora deben ser mayores a cero.")

    def calcular_pago(self):
        """Calcula el pago del contratista por horas trabajadas."""
        return self.horas_trabajadas * self.valor_hora

    def to_dict(self):
        """Serializa los datos del empleado contratista."""
        diccionario = super().to_dict()
        diccionario["horas_trabajadas"] = self.horas_trabajadas
        diccionario["valor_hora"] = self.valor_hora
        diccionario["tipo"] = "contratista"
        return diccionario

    def __str__(self):
        texto_padre = super().__str__()
        return f"{texto_padre} | Horas: {self.horas_trabajadas} | Pago: ${self.calcular_pago()}"


# ===========================
# 3. FUNCIONES JSON
# ===========================
def guardar_empleados(lista_empleados):
    """Guarda la lista de empleados en un archivo JSON."""
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(
                [empleado.to_dict() for empleado in lista_empleados],
                archivo,
                indent=4,
                ensure_ascii=False
            )
        print(" Empleados guardados exitosamente.")
    except IOError as e:
        print(f" Error al guardar: {e}")


def cargar_empleados():
    """Carga la lista de empleados desde un archivo JSON."""
    empleados_cargados = []

    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            listas_diccionarios = json.load(archivo)

        for datos in listas_diccionarios:
            if datos["tipo"] == "contratista":
                empleado = EmpleadoContratista(
                    datos["nombre"],
                    datos["salario"],
                    datos["departamento"],
                    datos["horas_trabajadas"],
                    datos["valor_hora"]
                )
            else:
                empleado = Empleado(
                    datos["nombre"],
                    datos["salario"],
                    datos["departamento"]
                )
            empleados_cargados.append(empleado)

        print(f" Se cargaron {len(empleados_cargados)} empleados desde el disco.")

    except FileNotFoundError:
        print("No se encontró archivo previo. Iniciando con lista vacía.")
    except json.JSONDecodeError:
        print(" El archivo JSON está corrupto.")

    return empleados_cargados


# ===========================
# 4. PRUEBA DE CAMPO
# ===========================
if __name__ == "__main__":
    print("--- 👥 SISTEMA DE EMPLEADOS ---\n")

    # Crear empleados
    emp1 = Empleado("Carlos Pérez", 3500000, "Sistemas")
    emp2 = Empleado("Ana Gómez", 4200000, "Contabilidad")
    cont1 = EmpleadoContratista("Luis Torres", 0, "Proyectos", 120, 45000)
    cont2 = EmpleadoContratista("Mario Ríos", 0, "Diseño", 80, 65000)

    lista = [emp1, emp2, cont1, cont2]

    # Mostrar todos
    print(" EMPLEADOS REGISTRADOS:")
    for e in lista:
        print(e)
        print(f"   Pago: ${e.calcular_pago()}")

    # Guardar
    print("\n")
    guardar_empleados(lista)

    # Cargar y mostrar
    print("\n EMPLEADOS RECARGADOS DESDE DISCO:")
    recargados = cargar_empleados()
    for e in recargados:
        print(e)
