"""
Ejercicio 3: @staticmethod
Objetivo:
Crear una clase Conversor con:

Un método estático celsius_a_fahrenheit() para convertir temperaturas.

Un método estático fahrenheit_a_celsius().

📝 Instrucciones:
Define la clase Conversor.

Implementa ambos métodos usando @staticmethod.

💡 Salida esperada:
        30°C a Fahrenheit: 86.0
        98°F a Celsius: 36.67
"""

class Conversor:
    
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return f"Conversión de celsius a fahrenheit: {celsius * 1.8 + 32}"
        
    @staticmethod
    def fahrenheit_a_celsius(fahrenheit):
        return f"Conversión de fahrenheit a celsius: {(fahrenheit - 32) * (5 / 9)}" 
    
fah = Conversor.celsius_a_fahrenheit(5)
cel = Conversor.fahrenheit_a_celsius(5)

print(fah)
print(cel)