from itertools import combinations

"""
Encuentra la sublista con la suma más alta
    Dada una lista de números enteros (positivos y negativos), encuentra la sublista contigua con la suma máxima.
    Por ejemplo, para la lista:
        numeros = [4, -1, 2, 1, -5, 4, 6, -3, 2]
    La sublista [4, -1, 2, 1, -5, 4, 6] tiene la mayor suma.
    Pista: Usa el algoritmo de Kadane.
"""
def kadane_maximo(numeros):
    suma_max = numeros[0]
    suma_actual = numeros[0]

    for num in numeros[1:]:
        suma_actual = max(num, suma_actual + num)
        suma_max = max(suma_max, suma_actual)
    return suma_max

numeros = [4, -1, 2, 1, -5, 4, 6, -3, 2]
suma = kadane_maximo(numeros)
print(suma)


"""
Generar todas las combinaciones posibles de una tupla
    Dada una tupla con valores únicos:
        tupla = (1, 2, 3, 4)
    Genera todas las combinaciones posibles de sus elementos en subconjuntos de tamaño 2 y 3.
    Pista: Usa itertools.combinations.
"""
tupla = (1, 2, 3, 4)
# lista = list(tupla)
combinacion_2 = list(combinations(tupla, 2))
combinacion_3 = list(combinations(tupla, 3))

print(f"combinación de tamaño 2: {combinacion_2}")
print(f"combinación de tamaño 3: {combinacion_3}")
