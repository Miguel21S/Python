from collections import Counter, defaultdict

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
diccionario["profesión"] = "Eng. Informático"
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

"""
Invertir un diccionario
    Dado el diccionario:
        diccionario = {"a": 1, "b": 2, "c": 3}
    Intercambia las claves y valores para obtener:
        {1: "a", 2: "b", 3: "c"}
"""
print("\n" + " Invertir un diccionario ".center(100, "="))

diccionario = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in diccionario.items()}
print(invertido)

"""
Agrupar elementos en un diccionario
    Dada la lista:
        alumnos = [("Juan", "A"), ("Ana", "B"), ("Pedro", "A"), ("Sofia", "B"), ("Luis", "C")]

Crea un diccionario donde las claves sean las letras de grupo ("A", "B", "C") y los valores sean listas con los nombres de los alumnos en ese grupo.
    Salida esperada:
        {"A": ["Juan", "Pedro"], "B": ["Ana", "Sofia"], "C": ["Luis"]}
"""
print("\n" + " Agrupar elementos en un diccionario ".center(100, "="))

alumnos = [("Juan", "A"), ("Ana", "B"), ("Pedro", "A"), ("Sofia", "B"), ("Luis", "C")]
grupos = {}
for nombre, grupo in alumnos:
    if grupo not in grupos:
        grupos[grupo] = []
    grupos[grupo].append(nombre)

print(grupos)

print("\n" + " Sugerencia ".center(100, "="))

print("\n"+" Sugerencia ".center(50, "="))
alumnos = [("Juan", "A"), ("Ana", "B"), ("Pedro", "A"), ("Sofia", "B"), ("Luis", "C")]
grupos = defaultdict(list)

for nombre, grupo in alumnos:
    grupos[grupo].append(nombre)
print(dict(grupos)) 

"""
Diccionario de frecuencia con palabras
    Dado el siguiente texto:
        texto = "python es un lenguaje de programación y python es muy popular"
    Crea un diccionario donde las claves sean las palabras y los valores la cantidad de veces que aparecen en el texto.
"""
print("\n" + " Diccionario de frecuencia con palabras ".center(100, "="))

texto = "python es un lenguaje de programación y python es muy popular"
conteo = Counter(texto.split(" "))
dicc = dict(conteo)
print(dicc)


