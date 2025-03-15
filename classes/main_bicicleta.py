import Bicicleta

bici = Bicicleta.Bicicleta("Amarelo", "Bic-21", 2018, 100)
print(bici)

bici.buzinar()
print(bici.parar(3))

print(bici.aumenta_velocidade(5))
print(bici.aumenta_velocidade(3))

print(bici.diminuir_velocidad(2))

print(bici.tipos_de_velocidades(-5, 3))