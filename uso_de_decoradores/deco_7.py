""" 
Ejercicio 7: @staticmethod para validación
Objetivo:
Crear una clase Validador con:

Un método estático es_numero() que devuelva True si una cadena representa un número, False en caso contrario.

📝 Instrucciones:
Usa @staticmethod para crear es_numero().

Prueba con diferentes cadenas.

💡 Salida esperada:
        ¿Es un número "123"? True
        ¿Es un número "abc"? False
"""

class Validador:
    @staticmethod
    def es_numero(numero):
        try:
            float(numero)
            return True
        except ValueError:
            return False
    
print(f"¿Es un número '123'? {Validador.es_numero('123')}")
print(f"¿Es un número 'abc'? {Validador.es_numero('abc')}")
print(f"¿Es un número '12.3'? {Validador.es_numero('12.3')}")
print(f"¿Es un número '874'? {Validador.es_numero('874')}")
print(f"¿Es un número '-45'? {Validador.es_numero('-45')}")
print(f"¿Es un número '1e3'? {Validador.es_numero('1e3')}")
