""" 
Ejercicio 10: Sistema de empleados avanzado
Objetivo:
Crear una clase base Empleado con:

Métodos comunes como calcular_salario().

Subclases EmpleadoTiempoCompleto y EmpleadoPorHora.

Usa @abstractmethod para calcular_salario() en la clase base.

📝 Instrucciones:
Usa @abstractmethod para hacer obligatorio calcular_salario().

Implementa salarios fijos para EmpleadoTiempoCompleto y por horas trabajadas para EmpleadoPorHora.

💡 Salida esperada:
        Salario del empleado a tiempo completo: 3000
        Salario del empleado por hora (20h x 15€): 300
"""
from abc import ABC, abstractmethod
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_fijo = 3000):
        self.salario_fijo = salario_fijo
      
    def calcular_salario(self):
        return f"Salario del empleado a tiempo completo: {self.salario_fijo}€"

class EmpleadoPorHora(Empleado):
    def __init__(self, horas_trabajadas, salario_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.salario_por_hora = salario_por_hora
        
    def calcular_salario(self):
        salario = self.horas_trabajadas * self.salario_por_hora
        return f"Salario del empleado por hora ({self.horas_trabajadas}h x {self.salario_por_hora}€): {salario}€"

empl_1 = EmpleadoTiempoCompleto()
print(empl_1.calcular_salario())

empl_2 = EmpleadoPorHora(20, 15)
print(empl_2.calcular_salario())