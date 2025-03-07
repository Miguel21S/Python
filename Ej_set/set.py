
"""
Ejercicios con Sets (Conjuntos)
    Operaciones con sets
        Crea dos conjuntos:
        Encuentra la intersección.
        Encuentra la unión.
        Encuentra la diferencia entre set1 y set2.
"""
print("\n" + " Operaciones con sets ".center(50, "="))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.intersection(set2)
print(f"La intersección entre los dos conjuntos: {set3}")
set3 = set1.union(set2)
print(f"La unión entre los dos conjuntos: {set3}")
set3 = set1.difference(set2)
print(f"La diferencia entre los dos conjuntos: {set3}")

"""
Ejercicios con Sets (Conjuntos)
    Eliminar duplicados de una lista usando un set
        Crea una lista con valores repetidos, por ejemplo: [1, 2, 2, 3, 4, 4, 5].
        Convierte la lista en un set para eliminar los duplicados.
        Convierte el set de nuevo en una lista y muéstrala.
"""
print("\n" + " Eliminar duplicados de una lista usando un set ".center(70, "="))

lista = [1, 2, 2, 3, 4, 4, 5]
elim = list(set(lista))
print(elim)

"""
Operaciones avanzadas con sets
    Crea un conjunto con los primeros 10 múltiplos de 3.
    Crea otro conjunto con los primeros 10 múltiplos de 5.
    Encuentra los números que son múltiplos de 3 y 5 a la vez.
"""
print("\n" + " 1º 10 múltiplos de 3, 1º 10 múltiplos de 5 y múltiplos de 3 y 5 a la vez ".center(100, "="))

set_1 = {3 * i for i in range(1, 11)}
set_2 = {5 * i for i in range(1, 11)}
interseccion = set_1 & set_2

print(f"Múltiplo de 3: {set_1}")
print(f"Múltiplo de 5: {set_2}")
print(f"Múltiplo de 3 y 5 a la vez: {interseccion}")

