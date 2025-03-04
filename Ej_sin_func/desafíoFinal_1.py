import random
"""Crea un programa que simule un sistema de acceso donde:

Verifique nombre de usuario y contraseña.
Valide si el usuario es administrador o visitante.
Permita realizar ciertas acciones solo si el usuario es admin.
"""

print("Bievenido al juego de valores aleatorios")
print("________________________________________________________________________________________________")
print("Los valores seran de 0 a 10 si acertas un valor sumas 2 puntos y si no te restas 3 punto y de no tener mas vidas terminas pierdes el juego")
print("________________________________________________________________________________________________")

usuarios = {
    "admin": {"clave": "1234", "rol": "admin"},
    "usuario": {"clave": "abc", "rol": "visitante"}
}

nombre = input("Digite su nombre: ")

if nombre in usuarios:
    clave = input("Digite la clave: ")

    if clave == usuarios[nombre]["clave"]:
        rol = usuarios[nombre]["rol"]
        print(f"Bienvenido, {nombre}. Rol: {rol}")

        punto_inicial = 10 if rol == "admin" else 5
        print(f"Puntos iniciales: {punto_inicial}")

        nivel_juego = 5 if rol == "admin" else 7
        print(f"Tienes {nivel_juego} niveles")

        for ronda in range(nivel_juego):
            if punto_inicial <= 0:
                print("Haz perdido todos sus puntos 'Fin del juego'")
                break
            
            valor = int(input("Adivina el valor de 0 a 10: "))
            valor_aleatorio = random.randint(0, 10)

            if valor == valor_aleatorio:
                punto_inicial += 2
                print("Felicidades +2 puntos")
            else:
                punto_inicial -= 3
                print("Uups -3 puntos")
            
            if valor_aleatorio == 7:
                punto_inicial <<= 1
                print("Haz hacertado el número especia sus puntos se han duplicados")
            
            print(f"Puntos iniciales: {punto_inicial}")
            print(f"Valor aleatorio era : {valor_aleatorio}\n")

        print(f"Puntuación final: {punto_inicial}")
        if rol == "admin":
            print("Acceso a painel del Administrador")

    else:
        print("Clave incorrecta. Acceso denegado")
else:
    print("Usuario no encontrado")

