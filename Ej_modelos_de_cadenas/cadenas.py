
"""
1: Capitalizar una frase
Escribe un programa que pida al usuario una frase y la convierta en formato título (primera letra de cada palabra en mayúscula).

Ejemplo:
    Entrada: "bienvenido a la programación en python"
    Salida: "Bienvenido A La Programación En Python"

"""
print("______________________________________________CONVERTIR PRIMERAS LETRAS EN MAYÚSCULA___________________________________________________________")

print(input("Escribe una frase: ").title())

print("______________________________________________CONTAR APARICIONES DE UNA LETRA___________________________________________________________")
"""
2: Contar apariciones de una letra
Pide al usuario que ingrese una palabra y una letra. Luego, muestra cuántas veces aparece esa letra en la palabra.

Ejemplo:
    Entrada:
    Palabra: "banana"
    Letra: "a"
    Salida: "La letra 'a' aparece 3 veces en 'banana'."
"""
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")
conteo = palabra.count(letra)
print(f"La letra '{letra}' aparece {conteo} veces en '{palabra}'.")

print("_____________________________________________REEMPLAZAR PALABRA EN UNA ORACIÓN____________________________________________________________")
"""
3: Reemplazar palabras en una oración
Escribe un programa que solicite una oración y reemplace todas las apariciones de la palabra "malo" por "bueno".

Ejemplo:
    Entrada: "Este día es malo, pero no todo es malo."
    Salida: "Este día es bueno, pero no todo es bueno."
"""
texto = input("Escribe una oración: ")
print(texto.replace("malo", "bueno"))

print("____________________________________________VERIFICAR SI UN TEXTO ES NUMÉRICO_____________________________________________________________")
"""
4: Verificar si un texto es numérico
Pide al usuario que ingrese un texto y verifica si es completamente numérico o no.

Ejemplo:
    Entrada: "12345"
    Salida: "El texto es numérico."
"""
txt = input("Escribe un texto: ")
if txt.isnumeric():
    print("El texto es numérico")
else:
    print("El texto no es numérico")

print("____________________________________________INVERTIR MAYÚSCULAS Y MINÚSCULAS_____________________________________________________________")
"""
5: Invertir mayúsculas y minúsculas
Escribe un programa que pida al usuario un texto y cambie las mayúsculas por minúsculas y viceversa.

Ejemplo:
    Entrada: "PyThOn Es Genial"
    Salida: "pYtHoN eS gENIAL"
"""
print(input("Digite el texto: ").swapcase())

print("____________________________________________CREAR UN USUARIO CON NOMBRE Y APELLIDO_____________________________________________________________")
"""
6: Crear un usuario con nombre y apellido
Pide al usuario que ingrese su nombre y apellido. Luego, genera un nombre de usuario en minúsculas y sin espacios.

Ejemplo:
Entrada:
    Nombre: "Carlos"
    Apellido: "Gómez"
    Salida: "Usuario generado: carlos_gomez"
"""
nombre = input("Digite tú nombre: ").lower().strip()
apellido = input("Digite tú apellido: ").lower().strip()
Usuario = f"{nombre}_{apellido}"

print(f"Usuario generado: {usuario}")

