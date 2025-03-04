for i in range(5):
    numero = int(input(f"Ingreso {i+1}/5 - Digita un número: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
