
"""
Ejercicios con Sets (Conjuntos)
    Operaciones con sets
        Crea dos conjuntos:
        Encuentra la intersección.
        Encuentra la unión.
        Encuentra la diferencia entre set1 y set2.
"""
eje = " Operaciones con sets "
print(eje.center(50, "="))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.intersection(set2)
print(f"La intersección entre los dos conjuntos: {set3}")
set3 = set1.union(set2)
print(f"La unión entre los dos conjuntos: {set3}")
set3 = set1.difference(set2)
print(f"La la diferencia entre los dos conjuntos: {set3}")


"""
Ejercicios con Sets (Conjuntos)
    Eliminar duplicados de una lista usando un set
        Crea una lista con valores repetidos, por ejemplo: [1, 2, 2, 3, 4, 4, 5].
        Convierte la lista en un set para eliminar los duplicados.
        Convierte el set de nuevo en una lista y muéstrala.
"""
eje = " Eliminar duplicados de una lista usando un set "
print(eje.center(70, "="))

lista = [1, 2, 2, 3, 4, 4, 5]
elim = set(lista)
lista = list(elim)
print(lista)