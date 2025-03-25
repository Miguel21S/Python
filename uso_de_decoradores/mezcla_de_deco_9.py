"""
Ejercicio 9: Mezclando decoradores
Objetivo:
Crear una clase Temperatura que tenga:

Un atributo privado _celsius.

Un @property para leer la temperatura en Celsius.

Un setter para validar el rango entre -273.15 y 1000.

Un @classmethod desde_fahrenheit() para crear un objeto a partir de Fahrenheit.

Un @staticmethod para validar si una temperatura está en estado de congelación (≤ 0 °C).

📝 Instrucciones:
Usa los cuatro decoradores.

Asegúrate de validar los límites.

💡 Salida esperada:
    Temperatura: 25°C
    Desde Fahrenheit (32°F): 0°C
    ¿Está en congelación? True
"""
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        
    def __str__(self):
        return f"Temperatura: {self.celsius}°C"
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, rango):
        if -273.15 <= rango <= 1000:
            self._celsius = rango
        else:
            raise ValueError("La temperatura debe estar entre -273.15°C y 1000°C.")
            
    @classmethod
    def desde_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) / 1.8
        return cls(celsius)
    
    @staticmethod
    def congelado(temp):
        return temp <= 0

try:        
    temp = Temperatura(-500)
    print(temp)
except ValueError as e:
    print(e)

try:
    temp_f = Temperatura.desde_fahrenheit(32)
    print(f"Desde Fahrenheit (32°F): {temp_f.celsius}°C")
except ValueError as e:
    print(e)

print(f"¿Está en congelación? {Temperatura.congelado(temp_f.celsius)}")