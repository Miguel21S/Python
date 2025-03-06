from collections import Counter

"""
Ejercicios con Diccionarios
    Crear y modificar un diccionario
        Crea un diccionario con 3 claves: "nombre", "edad" y "ciudad".
        Asigna valores a cada clave.
        Modifica la edad.
        Agrega una nueva clave "profesión".
"""
print("\n" + " Crear y modificar un diccionario ".center(50, "="))

diccionario = {"nombre": "Miguel", "edad": 22, "ciudad": "Valencia"}
diccionario.update({"edad": 23})
diccionario.update({"profesión": "Eng. Informático"})
print(diccionario)

"""
Recorrer un diccionario
    Usa un bucle for para recorrer un diccionario e imprimir sus claves y valores.
        persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
"""
print("\n" + " Recorrer un diccionario ".center(50, "="))
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

for clave, valor in persona.items():
    print(f"{clave} : {valor}")

"""
Contar la frecuencia de elementos en una lista usando un diccionario
    Dada la lista ["manzana", "pera", "manzana", "naranja", "pera", "manzana"], cuenta cuántas veces aparece cada fruta usando un diccionario.
"""
print("\n" + " Contar la frecuencia de elementos en una lista usando un diccionario ".center(100, "="))

lista = ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]
conteo = Counter(lista)

print(conteo)