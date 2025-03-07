from itertools import combinations

"""
Encuentra la sublista con la suma más alta
    Dada una lista de números enteros (positivos y negativos), encuentra la sublista contigua con la suma máxima.
    Por ejemplo, para la lista:
        numeros = [4, -1, 2, 1, -5, 4, 6, -3, 2]
    La sublista [4, -1, 2, 1, -5, 4, 6] tiene la mayor suma.
    Pista: Usa el algoritmo de Kadane.
"""
print("\n" + " Encuentra la sublista con la suma más alta ".center(70, "="))
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
print("\n" + " Generar todas las combinaciones posibles de una tupla ".center(70, "="))

tupla = (1, 2, 3, 4)
# lista = list(tupla)
combinacion_2 = list(combinations(tupla, 2))
combinacion_3 = list(combinations(tupla, 3))

print(f"combinación de tamaño 2: {combinacion_2}")
print(f"combinación de tamaño 3: {combinacion_3}")

"""
Encuentra la secuencia más larga de números consecutivos en un set
    Dado un conjunto de números desordenados:
        numeros = {100, 4, 200, 1, 3, 2, 101, 102, 5, 6}
    Encuentra la secuencia más larga de números consecutivos.
    En este caso, la secuencia más larga es [1, 2, 3, 4, 5, 6] con longitud 6.
    Pista: Un enfoque eficiente usa un set y evita ordenar la lista directamente.
"""
print("\n" + " Encuentra la secuencia más larga de números consecutivos en un set ".center(100, "="))

def sequencias(numeros):
    numeros_set = set(numeros)
    maximo_lon = 0
    mejor_sequencia = []

    for num in numeros:
        if num - 1 not in numeros_set:
            sequencia_actual = []
            actual = num
            
            while actual in numeros_set:
                sequencia_actual.append(actual)
                actual += 1
                
            if len(sequencia_actual) > maximo_lon:
                maximo_lon = len(sequencia_actual)
                mejor_sequencia = sequencia_actual

    return mejor_sequencia

numeros = {100, 4, 200, 1, 3, 2, 101, 102, 5, 6}
resultado = sequencias(numeros)
print(f"Tamaño de la sequencia: {len(resultado)}")
print(f"Mejor sequencia: {resultado}")