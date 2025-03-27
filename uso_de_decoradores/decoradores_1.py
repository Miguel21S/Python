"""
    Ejercicio 1: @property
Objetivo:
Crear una clase Rectangulo que tenga:

Atributos ancho y alto.

Un @property llamado area para calcular el área automáticamente.

Un setter para asegurar que ancho y alto no sean negativos.

📝 Instrucciones:
Define la clase Rectangulo.

Usa @property para crear un atributo calculado area.

Usa @ancho.setter y @alto.setter para validar los valores.

💡 Salida esperada:
        Área del rectángulo: 20
        Nuevo ancho: 10
        Área actualizada: 40
"""


class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    @property
    def ancho(self):
        return self._ancho    

    @ancho.setter
    def ancho(self, nuevo_ancho):
        if nuevo_ancho < 0:
            raise ValueError("El valor del ancho no puede ser negativo")
        
        self._ancho = nuevo_ancho
        
    @property
    def alto(self):
        return self._alto
      
    @alto.setter
    def alto(self, nuevo_alto):
        if nuevo_alto < 0:
            raise ValueError("El valor del alto no puede ser negativo")
        
        self._alto = nuevo_alto   
        
    @property
    def area(self):
        return self._alto * self._ancho   

try:
    rectangulo = Rectangulo(2, 2)
    print(f"Resultado del area: {rectangulo.area}")
except ValueError as e:
    print(e)

try:
    rectangulo.ancho = 2
    rectangulo.alto = 4
    print(f"Ancho: {rectangulo.ancho}\nAlto: {rectangulo.alto}")
    print(f"Nuevo resultado: {rectangulo.area}")
except ValueError as e:
    print(e)