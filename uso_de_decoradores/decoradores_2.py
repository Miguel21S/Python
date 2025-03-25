"""
    Ejercicio 2: @classmethod
Objetivo:
Crear una clase Empleado con:

Atributos nombre y salario.

Un contador de empleados.

Un método de clase contar_empleados() que devuelva el total de empleados.

📝 Instrucciones:
Define la clase Empleado.

Usa un atributo de clase total_empleados.

Implementa el método contar_empleados() usando @classmethod.

💡 Salida esperada:
        Total de empleados: 2
"""

class Empleado:
    total_empleados = 0

    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario
        
        Empleado.total_empleados += 1
        
    @classmethod
    def contar_empleados(cls):
        return (f"Total de empleados: {cls.total_empleados}")

empleado_1 = Empleado("Miguel", 2500)
empleado_2 = Empleado("Simão", 2500)
print(empleado_1._nombre)

print(Empleado.contar_empleados())