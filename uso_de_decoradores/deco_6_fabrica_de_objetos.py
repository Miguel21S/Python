""" 
Ejercicio 6: @classmethod como fábrica de objetos
Objetivo:
Crear una clase Producto con:

Atributos: nombre, precio.

Un método desde_string() que permita crear objetos a partir de un string en formato "nombre,precio".

📝 Instrucciones:
Usa @classmethod para implementar desde_string().

Crea varios productos a partir de cadenas.

💡 Salida esperada:
        Producto: Televisor - Precio: 750
        Producto: Laptop - Precio: 1200
"""

class Producto:    
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = float(precio)
        
    def __str__(self):
        return f"Producto: {self._nombre} - Precio: {self._precio:.2f}"
    
    @classmethod 
    def desde_string(cls, cadena):
        nombre, precio = cadena.split(",")
        return cls(nombre.strip(), float(precio.strip()))

prod_1 = Producto.desde_string("Computador, 1500")
prod_2 = Producto.desde_string("Televiso, 800.45")
prod_3 = Producto.desde_string("Laptop, 1200")

print(prod_1)
print(prod_2)
print(prod_3)