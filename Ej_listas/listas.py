from collections import Counter

"""
Ejercicios Básicos
Agregar y eliminar elementos
    Crea una lista vacía.
    Agrega los números del 1 al 5 usando.
    Elimina el último elemento.
    Inserta el número 100 en la segunda posición.
"""
t = " Agregar y eliminar elementos "
print(t.center(50, "="))
lista = []
i = 0
while i < 5:
    nuemros = int(input(f"Digite 5 números de {i+1}/5: "))
    lista.append(nuemros)
    i += 1

lista.pop()
lista.insert(1, 100)   
print(lista)

"""
Ordenar listas
    Crea una lista con los números [3, 1, 4, 1, 5, 9, 2].
    Ordena la lista de forma ascendente.
    Invierte el orden de la lista.
"""
t = " Ordenar listas "
print(t.center(50, "="))

numeros = [3, 1, 4, 1, 5, 9, 2]
print(f"Lista principal: {numeros}")

numeros.sort()
print(f"Lista ordenado: {numeros}")

numeros.reverse()
print(f"Lista de orden invertida: {numeros}")

"""
Contar elementos
    Dada la lista ['manzana', 'banana', 'naranja', 'banana', 'uva', 'banana'],
    cuenta cuántas veces aparece 'banana' usando.
"""
t = " Contar elementos "
print(t.center(50, "="))

lista = ['manzana', 'banana', 'naranja', 'banana', 'uva', 'banana']
print(lista.count("banana"))

"""
Extender listas
    Crea dos listas: a = [1, 2, 3] y b = [4, 5, 6].
    Une las listas.
    Usa + para concatenarlas y compara los resultados.
"""
t = " Extender listas "
print(t.center(50, "="))

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_concatenada = lista_1 + lista_2
print(f"Unión concatenada con + {lista_concatenada}")

lista_1.extend(lista_2)
print(f"Unión extend de las listas {lista_1}")

"""
Ejercicios Intermedios
Eliminar duplicados
    Escribe un programa que elimine los valores duplicados de la lista [1, 2, 2, 3, 4, 4, 5, 6, 6] manteniendo el orden original.
"""
t = " Eliminar duplicados "
print(t.center(50, "="))

lista = [1, 2, 2, 3, 4, 4, 5, 6, 6]
lista_sin_duplicados = []

for num in lista:
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)

print(lista_sin_duplicados)

"""
Filtrar elementos
    Dada la lista [10, 25, 30, 45, 60, 75, 90], usa una comprensión de listas para obtener solo los números mayores a 50.
"""
t = " Filtrar elementos "
print(t.center(50, "="))

lista = [10, 25, 30, 45, 60, 75, 90]

filtrar = [num for num in lista if num > 50]
print(f"Números mayores a 50: {filtrar}")

"""
Unir palabras en una cadena
    Dada la lista ['Hola', 'mundo', 'Python', 'es', 'genial'], usa .join() para convertirla en una sola cadena separada por espacios.
"""
t = " Unir palabras en una cadena "
print(t.center(50, "="))

lista = ['Hola', 'mundo', 'Python', 'es', 'genial']
print(" ".join(lista))

"""
Dividir una cadena en palabras
    Usa .split() para convertir la cadena "Aprender Python es divertido" en una lista de palabras.
"""
t = " Dividir una cadena en palabras "
print(t.center(50, "="))

texto = "Aprender Python es divertido"
print(texto.split(" "))

"""
Ejercicios Avanzados
Rotar una lista
    Dada una lista [1, 2, 3, 4, 5], mueve el primer elemento al final usando .pop() y .append().
"""
t = " Rotar una lista "
print(t.center(50, "="))

lista = [1, 2, 3, 4, 5]
primero = lista.pop(0)
lista.append(primero)
print(lista)

"""
Obtener los elementos únicos
    Escribe una función que reciba una lista con números repetidos y devuelva otra lista solo con los valores únicos (sin usar set()).
"""
t = " Obtener los elementos únicos "
print(t.center(50, "="))

def elementos_unicos(lista):
    count = Counter(lista)
    valores_unicos = [num for num in lista if count[num] == 1]
    return f"Lista de valores únicos {valores_unicos}"

lista = [2, 3, 3, 5, 8, 2, 9, 12, 7, 66, 8]
lista_num_uni = elementos_unicos(lista)
print(lista_num_uni)

"""
Reemplazar valores en una lista
    Dada la lista [1, 2, 3, 4, 5], reemplaza el número 3 por el 100 usando su índice.
"""
t = " Reemplazar valores en una lista "
print(t.center(50, "="))

lista = [1, 2, 3, 4, 5]
lista[2] = 100
print(lista)

"""
Comprobar si una lista está ordenada
    Escribe una función que reciba una lista y devuelva True si está ordenada de manera ascendente y False en caso contrario.
"""
t = " Comprobar si una lista está ordenada "
print(t.center(50, "="))

def lista_ordenada_true(lista):
    return lista == sorted(lista)

lista = [1, 2, 3, 4, 5]
lista_ = lista_ordenada_true(lista)
print(lista_)

"""
Suma y promedio de una lista
    Crea una lista con 5 números enteros.
    Calcula la suma de todos los números.
    Calcula el promedio y muestra el resultado.    
"""
print("\n" + " Suma y promedio de una lista ".center(50, "="))

lista = [45, 21, 3, 64, 5]
suma = sum(lista)
promedio = suma / len(lista)
print(f"La suma de los valores de la lista: {suma}\nEl promedio de la suma: {promedio}")
