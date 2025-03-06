
"""
Ejercicios con Tuplas
    Acceder a elementos de una tupla
        Crea una tupla con los nombres de 3 ciudades.
        Muestra el primer y el último elemento.

    Conversión de lista a tupla
        Crea una lista con los valores [10, 20, 30, 40].
        Convierte la lista en una tupla.
        Muestra la tupla resultante.

    Concatenar tuplas
        Crea dos tuplas: tupla1 = (1, 2, 3) y tupla2 = (4, 5, 6).
        Une ambas tuplas en una nueva tupla.
"""
print()
eje = " Acceder a elementos de una tupla "
print(eje.center(50, "="))

tupla = ("New York", "Miami", "Las Vegas")
elementos = f"{tupla[0]}, {tupla[2]}"
print(elementos)

eje = " Conversión de lista a tupla "
print(eje.center(50, "="))

lista = [10, 20, 30, 40]
tupla = tuple(lista)
print(tupla)

eje = " Concatenar tuplas "
print(eje.center(50, "="))

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla3 = tupla1 + tupla2
print(tupla3)
