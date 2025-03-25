
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