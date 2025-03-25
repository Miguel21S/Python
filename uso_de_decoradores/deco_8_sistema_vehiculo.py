""" 
Ejercicio 8: @abstractmethod para un sistema de vehículos
Objetivo:
Crear una clase abstracta Vehiculo con:

Un método abstracto mover().

Subclases Auto y Avion que lo implementen.

📝 Instrucciones:
Usa ABC y @abstractmethod para mover().

Implementa diferentes formas de moverse para Auto y Avion.

💡 Salida esperada:
        El auto se mueve por carretera.
        El avión vuela por el cielo.
"""
from abc import ABC, abstractmethod
class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Auto(Vehiculo):
    # def __init__(self, adelante = True, atras = False):
    #     self._adelante = adelante
    #     self._atras = atras
        
    # def mover(self):
    #     if self._adelante:
    #         return f"El Auto se mueve hacia adelante"
    #     else:
    #         return f"El Auto se mueve hacia atras"
    
    def mover(self):
        return "El auto se mueve por carretera"

class Avion(Vehiculo):
    # def __init__(self, carretera = True, cielo = False):
    #     self.carretera = carretera
    #     self.cielo = cielo
        
    # def mover(self):
    #     if self.carretera:
    #         return f"El Avión se mueve hacia carretera"
    #     else:
    #         return f"El Avión vuela por el cielo "
    
    def mover(self):
        return "El avión vuela por el cielo."

auto = Auto()       
print(auto.mover()) 
avion = Avion()
print(avion.mover()) 


# adelante = False
# atras = False

# auto = Auto(adelante, atras)
# print(auto.mover())

# carretera = False
# cielo = False
# avion = Avion(carretera, cielo)
# print(avion.mover())