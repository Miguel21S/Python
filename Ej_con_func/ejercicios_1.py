import math

"""
Ejercicio 1: Saludo personalizado
Crea una función llamada saludar_usuario que reciba un nombre como argumento y devuelva un mensaje de saludo.
🔹 Ejemplo de uso:
                    mensaje = saludar_usuario("Ana")
                    print(mensaje)
🔹 Salida esperada:
                    ¡Hola, Ana! Bienvenido/a.
"""
def saludar_usuario(nombre):
    return f"¡Hola, {nombre}! Bienvenido/a."

mensaje = saludar_usuario(input("Digite tú nombre: "))
print(f"{mensaje}")

print("_______________________________________________________________________")

"""
Ejercicio 2: Calculadora de suma
Escribe una función sumar que reciba dos números como argumentos, los sume y devuelva el resultado.
🔹 Ejemplo de uso:
                    resultado = sumar(4, 7)
                    print(resultado)
🔹 Salida esperada:
                    11
"""
def suma(num1, num2):
    return num1 + num2

num1 = float(input("Digite 1º valor: "))
num2 = float(input("Digite 2º valor: "))
resultado = suma(num1, num2)
print(f"la suma de los dos valore es: {resultado}")
print("_______________________________________________________________________")

"""
Ejercicio 3: Número par o impar
Define una función es_par que reciba un número y devuelva True si es par y False si es impar.
🔹 Ejemplo de uso:
                    print(es_par(8))  # True
                    print(es_par(3))  # False
"""

def es_par(valor):
    return valor % 2 == 0

num = int(input("Digite el valor para saber si es par o impar: "))
print(es_par(num))
print("_______________________________________________________________________")

"""
Ejercicio 4: Área de un círculo
Crea una función calcular_area_circulo que reciba el radio de un círculo y devuelva su área. Usa la fórmula:
[ Área = π × radio^2 ]
 
Usa math.pi para obtener el valor de π.
🔹 Ejemplo de uso:
                    area = calcular_area_circulo(5)
                    print(area)
"""
def calcular_area_circulo(radio):
    return ((math.pi) * (radio ** 2))

radio = float(input("Digite el valor del area: "))
area = calcular_area_circulo(radio)

print(f"Cálculo de area de un circulo {area}")
print("_______________________________________________________________________")

"""
Ejercicio 1: Conversión de temperatura
Crea una función llamada celsius_a_fahrenheit que convierta una temperatura de grados Celsius a Fahrenheit usando la fórmula:
F=(C×9/5)+32
🔹 Ejemplo de uso:
                    temperatura_f = celsius_a_fahrenheit(25)
                    print(temperatura_f)  # 77.0
"""
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Digite el valor del Celsius: "))
temperatura_f = celsius_a_fahrenheit(celsius)
print(f"El valor de la conversión de temperatua a Fahrenheit {temperatura_f}")
print("_______________________________________________________________________")

"""
Ejercicio 2: Factorial de un número
Crea una función factorial(n) que reciba un número entero positivo y devuelva su factorial.
Recuerda que el factorial de un número se calcula como:
n!=n * (n - 1) * (n - 2) * ... * 1
🔹 Ejemplo de uso:
                    print(factorial(5))  # 120
"""
def factorial(valor):
    resultado = 1
    for i in range(1, valor + 1):
        resultado *= i
    return resultado

numero = int(input("Digite el valor del factoria: "))
resultado = factorial(numero)
print(f"Factorial de {numero}! = {resultado}")
print("_______________________________________________________________________")

"""
Ejercicio 3: Contar vocales en una palabra
Crea una función contar_vocales(palabra) que reciba una palabra y devuelva el número de vocales (a, e, i, o, u) que contiene.
🔹 Ejemplo de uso:
                    print(contar_vocales("Python"))  # 1
                    print(contar_vocales("Elefante"))  # 4
"""
def contar_vocales(palabra):
    vocales = ("aeiou")
    return sum(1 for vocal in palabra.lower() if vocal in vocales)

vocales = contar_vocales(input("Escribe la palabra: "))
print(f"La palabra tiene {vocales} vocales")
print("_______________________________________________________________________")

"""
Ejercicio 4: Número primo
Crea una función es_primo(n) que determine si un número es primo o no.
Un número primo es aquel que solo es divisible por 1 y por sí mismo.
🔹 Ejemplo de uso:
                    print(es_primo(7))  # True
                    print(es_primo(10))  # False
"""
def es_primo(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Digite el nº para saber si es primo o no: "))
primo = es_primo(numero)
print(primo)

