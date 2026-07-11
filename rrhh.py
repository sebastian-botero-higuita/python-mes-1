class Empleado:
    def __init__(self, nombre, cargo, salario_base, bonificacion):
        """Inicializa un empleado con sus datos basicos verificados.
        primero se asigna el estado al objeto, luego se valida de forma interna."""
        
        self.nombre = nombre
        self.cargo = cargo
        self.salario_base = salario_base
        self.bonificacion = bonificacion

        # Escudo de validacion interna sobre los atributos del objeto
        if self.salario_base < 0 or self.bonificacion < 0:
            raise ValueError("Los valores financieros no pueden ser negativos.")
        
    def calcular_salario_neto(self):
        """Retorna el dinero total que recibe el empleado."""
        return self.salario_base + self.bonificacion
    