"""
Ejercicio 4: @abstractmethod
Objetivo:
Crear una clase abstracta Forma con:

Un método abstracto area().

Dos clases Circulo y Cuadrado que lo implementen.

📝 Instrucciones:
Usa ABC y @abstractmethod para definir la clase Forma.

Implementa las subclases Circulo y Cuadrado.

Calcula el área de un círculo y un cuadrado.

💡 Salida esperada:
        Área del círculo: 78.54
        Área del cuadrado: 25
"""

from abc import ABC, abstractmethod
import math

class Forma(ABC): 
    @abstractmethod
    def area(self):
        pass
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return  math.pi * self.raio ** 2
    
class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
d = Circulo(2)
print(d.area())

c = Cuadrado(4)
print(c.area())