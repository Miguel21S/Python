import random

# EJERCICIOS DE COMPRENSIONES DE LISTAS (ENFOCADOS EN CREAR LISTAS DE FORMA EFICIENTE)

"""
1) Números pares del 1 al 50:
Crea una lista con todos los números pares entre 1 y 50.
"""
print("")

lista_de_numeros = [num for num in range(1, 51) if num % 2 == 0];
print(f"Números paras del 1 al 50: {lista_de_numeros}")
print("__________________________________________________________________")
print("")

"""
2) Filtrar palabras cortas:
Dada la lista palabras = ["sol", "computadora", "cielo", "luz", "universo"], crea otra lista con palabras que tengan menos de 5 letras.
"""
palabras = ["sol", "computadora", "cielo", "luz", "universo"];

palabras_cortas = [pal for pal in palabras if len(pal) < 5]

print(f"Lista principal: {palabras}")
print(f"Lista de palabras de menos de 5 letras: {palabras_cortas}")

print("__________________________________________________________________")
print("")

"""
3) Cuadrados de números:
Crea una lista con los cuadrados de los números del 1 al 10.
Ejemplo: [1, 4, 9, 16, 25, ...]
"""
lista_de_cuadrado = [num**2 for num in range(1, 11)]
print(f"Lista de números cuadrados del 1 al 10: {lista_de_cuadrado}")

print("__________________________________________________________________")
print("")

"""
4) Números divisibles por 3:
Genera una lista de números del 1 al 100 que sean divisibles por 3.
"""
numeros_divisible3 = [num for num in range(1, 101) if num % 3 == 0]
print(f"Números divisibles por 3: {numeros_divisible3}")
print("__________________________________________________________________")
print("")

# EJERCICIOS DE BUCLES TRADICIONALES (PERFECTOS PARA LÓGICA MÁS COMPLEJA Y FLUJOS DE CONTROL)
"""
1) Juego de adivinar el número:

Genera un número aleatorio entre 1 y 20.
El usuario debe adivinarlo.
Por cada intento fallido, dale una pista: "Mayor" o "Menor".
"""
print("__________________________________________________________________")
print("")

valor_aleatorio = random.randint(1, 20)
intentos = 0

while True:
    valor = int(input("Adivina el número del 1 a 20: "))
    intentos += 1

    if valor == valor_aleatorio:
        print(f"¡Felicidades haz ganado! en {intentos} intentos")
        break

    else:
        n_aleatorio = "Valor es Mayor" if valor > valor_aleatorio else "Valor es Menor"
        print(f"Valor aleatorio es: {n_aleatorio}")
        print("Intenta de nuevo:")
print("__________________________________________________________________")
print("")

"""
2) Contador de vocales:
Pide al usuario que ingrese una frase y muestra cuántas vocales tiene.
Ejemplo: "Hola Mundo" ➔ 4 vocales
"""

frase = input("Ingrese una frase: ").lower()
vocales = ("aeiou")
contador = sum(1 for letra in frase if letra in vocales)

print(f"La frase tiene {contador} vocales.")
print("__________________________________________________________________")
print("")

"""
3) Filtrar números primos:
Pide al usuario que ingrese 10 números y crea una nueva lista solo con los números primos.
"""
print("Ingresa 10 números:")
numero = [int(input("Ingresa el números: ")) for _ in range(10)]
n_primos = []

for num in numero:
    if num < 2:
        continue

    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
            n_primos.append(num)

print(f"Lista de números primos: {n_primos}")

print("__________________________________________________________________")
print("")

"""
4) Cajero automático simple:

Saldo inicial: $1000.
Opciones:
1. Consultar saldo
2. Ingresar dinero
3. Retirar dinero
4. Salir
El programa debe repetirse hasta que el usuario decida salir.
"""
print("Opciones")
print("1. Consultar saldo")
print("2. Ingresar dinero")
print("3. Retirar dinero")
print("4. Salir")

saldo_inicial = 1000
while True:
    valor = int(input("Digite el número de la operación: "))
    if valor > 0:
        if valor == 1:
            print(f"Saldo actual: {saldo_inicial}")

        elif valor == 2:
            s_ingresar = int(input("Digite valor a ingresar: "))

            saldo_inicial += s_ingresar
            print("Saldo ingresado con succeso ")
            print("Deseas realizar una otra operacion")
            
        elif valor == 3:
            s_retirar = int(input("Digite valor a retirar: "))

            if s_retirar <= saldo_inicial:
                saldo_inicial -= s_retirar

                print("Gracias por operar en nuestro banco")
                print("Deseas realizar una otra operacion")
            else:
                print("Tú saldo no es suficiente")
                print("Deseas realizar una otra operacion")

        elif valor == 4:
            break
        else:
            print("Ingresa un número del 1 a 4")
    else:
        print("Digite un número positivo: ")

print("Gracias por operar en nuestro banco regrese siempre")
            
