def saludar():
    print("Hola Mundo")

saludar()

def dimeNombre(nombre):
    print(f"Hola {nombre}")

dimeNombre("Miguel")

def suma(a, b):
    print(f"a + b = {a+b}")

suma(5, 5)

def suma1(a, b):
    return a + b;

recibirSuma1 = suma1(25, 5)
print(f"Recibido valor suma1 (25 + 5) = {recibirSuma1}")

print(f"Reusar el valor del suma1 (recibirSuma1 / 3) = {recibirSuma1 / 3}")

def calculcar_area(base, altura):
    return base * altura

area = calculcar_area(15, 4)
print(f"Cálcular area  15 * 4 = {area}")