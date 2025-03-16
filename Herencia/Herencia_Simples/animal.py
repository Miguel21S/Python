
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"{self.nombre}"

    def ladrar(self):
        print("Wuwuwuwuwu")
        
class Perro(Animal):
    def ladrar(self):
        print("Rirrrrrrrrrr")

perro = Perro("Rex")
print(perro.nombre)
perro.ladrar()

perro_1 = Animal("Rex_1")
print(perro_1)
perro_1.ladrar()