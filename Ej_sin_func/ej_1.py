# encoding:utf-8
import random
'''
nombre = input('Escribe el nombre: ')
edad = int(input('Escribe la edad: '))
print(f"{nombre} tienes {edad} años")
'''

# 1. Ejercicios de Operadores Aritméticos

print("________________Ejercicios de Operadores Aritméticos")
print("___________________________________________________________________________")
"""Calculadora básica
Crea un programa que solicite al usuario dos números y muestre la suma, resta, multiplicación, división, módulo, exponente y división entera.
"""
'''
numero_1 = int(input("Digite el 1º número: "))
numero_2 = int(input("Digite el 2º número: "))

print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
print(f"{numero_1} % {numero_2} = {numero_1 % numero_2}")
print(f"{numero_1} ** {numero_2} = {numero_1 ** numero_2}")

if numero_2 != 0:
    print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
    print(f"{numero_1} // {numero_2} = {numero_1 // numero_2}")
else:
    print("No se puede dividir por cero.")
print("___________________________________________________________________________")

"""Área de un triángulo
Pide la base y la altura de un triángulo al usuario y calcula su área (Área = (base * altura) / 2).
"""
base = float(input("Digite la base: "))
altura = float(input("Digite la altura: "))
area = ((base * altura) / 2)
print(f'Área (({base} * {altura}) / 2) = {area}')
print("____________________________________________________________________________")

"""Conversor de temperaturas
Convierte grados Celsius a Fahrenheit (F = C * 1.8 + 32) y Kelvin (K = C + 273.15).
"""
celsius = int(input("Digite el valor de Celsius: "))
f = celsius * 1.8 + 32
k = celsius + 273.15
print("grados Celsius a Fahrenheit")
print(f'{celsius} * 1.8 + 32 = {f}')
print("_____________________________")
print("grados Celsius a Kelvin")
print(f'{celsius} + 273.15 = {k}')
print("____________________________________________________________________________")

# 2. Ejercicios de Operadores de Comparación

print("_______________Ejercicios de Operadores de Comparación")
print("____________________________________________________________________________")
"""Número mayor
Escribe un programa que solicite tres números al usuario y determine cuál es el mayor.
"""
numero_1 = int(input("Digite el número: "))
numero_2 = int(input("Digite el número: "))
numero_3 = int(input("Digite el número: "))

if(numero_1 > numero_2 and numero_1 > numero_3):
    print(f"El 1º número es el mayor de todos {numero_1}")
elif(numero_2 > numero_3):
    print(f"El 2º número es el mayor de todos {numero_2}")
else:
    print(f"El 3º número es el mayor de todos {numero_3}")
print("____________________________________________________________________________")

"""Verificación de edad
Pide al usuario su edad y muestra si es mayor o menor de edad.
"""
edad = int(input("Digite tú edad: "))
if edad > 17:
    print(f"Eres mayor de edad")
else:
    print(f"Eres menor de edad")
print("____________________________________________________________________________")

"""Verificación de igualdad
Solicita dos cadenas de texto al usuario y verifica si son iguales ignorando mayúsculas/minúsculas.
"""
texto_1 = input("Digite el 1º texto: ")
texto_2 = input("Digite el 2º texto: ")
print(texto_1.lower() == texto_2.lower())
print("____________________________________________________________________________")

# 3. Ejercicios de Operadores Lógicos
print("________________Ejercicios de Operadores Lógicos")
print("___________________________________________________________________________")

"""Verificación de acceso
Crea un sistema que permita el acceso solo si el usuario tiene más de 18 años y tiene permiso de administrador.
"""
edad = int(input("Digite tú edad: "))
usuario = ["admin", edad]
if usuario[1] > 18 and usuario[0]=="admin":
    print("Accesso permitido")
    print("Eres Administrador")
else:
    print("Accesso denegado")

print("___________________________________________________________________________")
"""Número dentro de un rango
Pide al usuario un número y verifica si está entre 10 y 50.
"""
numero = int(input("Digite 1 número: "))
if numero >= 10 and numero <= 50:
    print("El número esta entre 10 y 50")
else:
    print("El número no esta entre 10 y 50")

print("___________________________________________________________________________")
"""Evaluación de notas
Pide tres calificaciones y determina si el estudiante aprobó (promedio ≥ 5) y si obtuvo una nota perfecta en alguna materia.
"""
prog = int(input("Digite la nota de Programación: "))
mat = int(input("Digite la nota de Matemática: "))
fis = int(input("Digite la nota de Física: "))

promedio = (prog + mat + fis) / 3
if promedio >= 5:
    print(f"Nota final {promedio} aprobado")
else:
    print(f"Nota final {promedio} desaprobado")

if prog > 10:
    print(f"Nota perfecta obtida en Programación")
elif mat > 10:
    print(f"Nota perfecta obtida en Matemática")
elif fis > 10:
    print(f"Nota perfecta obtida en Física")
else:
    print(f"No obtubo nota perfecta")

print("___________________________________________________________________________")

# 4. Ejercicios de Operadores de Asignación
print("________________Ejercicios de Operadores de Asignación")
print("___________________________________________________________________________")
"""Contador simple
Inicia una variable en 0 y usa operadores de asignación (+=, -=, *=, etc.) para actualizar su valor según diferentes operaciones.
"""
contador = 0;
contador += 1
print(f"Contador crecente:", contador)
contador *= 2
print(f"Contador multiple:", contador)
contador -= 1
print(f"Contador decrecente:", contador)

print("___________________________________________________________________________")

"""Descuento en productos
Pide al usuario el precio de un producto y aplica un descuento del 20% usando el operador *=.
"""
precio = int(input("Digite el precio: "))
precio *= 0.8
print(f"Descuento de: {precio}%")
print("___________________________________________________________________________")

"""Gestor de puntos
Simula un sistema de puntos donde el usuario puede sumar o restar puntos utilizando operadores de asignación.
"""
print("Al digitar el valor si acertas se te agrega 2 puntos y si no se te descuenta 4 puntos")
punto_inicial = 10;
valor = int(input("Digite un valor de 0 a 10: "))
aleatorio = random.randrange(0, 10)
if valor == aleatorio:
    punto_inicial += 2
    print(f"Has ganado + 2 puntos y acumulas un total de: {punto_inicial} puntos")
    print("Felicidades haz ganado")
else:
    punto_inicial -= 4
    print(f"Has perdido 4 puntos y acumulas un total de: {punto_inicial} puntos")

print("Valor mostrado es: ", aleatorio)
print("_________________________________________________________________________________")

# 5. Ejercicios de Operadores de Identidad y Membresía
print("________________Ejercicios de Operadores de Identidad y Membresía")
print("_________________________________________________________________________________")

"""Verificar objeto
Crea dos listas y verifica si apuntan al mismo objeto usando is y si tienen el mismo contenido usando ==.
"""
lista_1 = [2, 1, 5, 6]
lista_2 = [2, 1, 5, 6]
lista_2 = lista_1

print(f"Apuntan al mismo objecto: {lista_1 is lista_2}")
print(f"Tienen el mismo contenido: {lista_1 == lista_2}")
print("_________________________________________________________________________________")

"""Buscador de palabras
Solicita una palabra al usuario y verifica si se encuentra en una lista de palabras clave usando in.
"""
palabra = input("Escribe la palabra: ")
lista = ["Hola", "Quiero", "Amo", "Que"]

if palabra in lista:
    print("Es una palabra clave")
else:
    print("No es una palabra clave")
print("_________________________________________________________________________________")

"""Filtrar elementos
Dada una lista de números, crea una nueva lista solo con los números pares utilizando operadores de membresía.
"""
lista = [4, 5, 3, 7, 9, 8, 12, 14, 20, 30, 41]
lista_2 = [14, 12, 30, 4, 8, 20]

print(lista not in lista_2)
print("_________________________________________________________________________________")

# 6. Ejercicios de Operadores Bit a Bit
print("________________Ejercicios de Operadores Bit a Bit")
print("_________________________________________________________________________________")

"""Verificar paridad
Pide al usuario un número y usa el operador & para verificar si es par o impar.
"""
numero = int(input("Digite el número: "))

if numero & 1 == 0:
    print("es par")
else:
    print("no es par")
print("_________________________________________________________________________________")

"""Desplazamiento de bits
Pide un número al usuario y desplaza sus bits dos posiciones a la izquierda (<<) y dos posiciones a la derecha (>>).
"""

numero = int(input("Digite el número: "))
print(f"{numero} << 2 = {numero << 2} (desplazamiento a la izquierda)")
print(f"{numero} 2 >>= {numero >> 2} (desplazamiento a la derecha)")

print("_________________________________________________________________________________")

"""Contador binario
Crea un contador binario que incremente números de 0 a 15 y muestra su representación binaria usando bin().
"""

for numero in range(16):
    print(f"{numero} en binario es {bin(numero)}")
'''
                      
                        # Sugerencias para la mejora del código

# Operadores de Comparación:
"""Número mayor
Escribe un programa que solicite tres números al usuario y determine cuál es el mayor.
"""
numeros = [int(input("Digite el número: ")) for _ in range(3)]
print(f"El mayor es: {max(numeros)}")

"""Verificación de igualdad
Solicita dos cadenas de texto al usuario y verifica si son iguales ignorando mayúsculas/minúsculas.
"""
texto_1 = input("Digite el 1º texto: ").strip().lower()
texto_2 = input("Digite el 2º texto: ").strip().lower()
print("Son iguales" if texto_1 == texto_2 else "Son diferentes")

# 3. Operadores Lógicos:
"""Verificación de acceso
Crea un sistema que permita el acceso solo si el usuario tiene más de 18 años y tiene permiso de administrador.
"""
edad = int(input("Digite tu edad: "))
es_admin = input("¿Eres administrador? (sí/no): ").strip().lower() == "sí"

if edad > 18 and es_admin:
    print("Acceso permitido")
else:
    print("Acceso denegado")

"""Evaluación de notas
Pide tres calificaciones y determina si el estudiante aprobó (promedio ≥ 5) y si obtuvo una nota perfecta en alguna materia.
"""
notas = [int(input(f"Digite la nota de {materia}: ")) for materia in ["Programación", "Matemática", "Física"]]
promedio = sum(notas) / len(notas)
estado = "aprobado" if promedio >= 5 else "desaprobado"
print(f"Nota final {promedio} - {estado}")

if 10 in notas:
    print("¡Nota perfecta en alguna materia!")

# 5. Operadores de Identidad y Membresía:
"""Filtrar elementos
Dada una lista de números, crea una nueva lista solo con los números pares utilizando operadores de membresía.
"""
numeros = [4, 5, 3, 7, 9, 8, 12, 14, 20, 30, 41]
pares = [num for num in numeros if num % 2 == 0]
print(f"Números pares: {pares}")

