
class Mamifero:
    def amamentar(self):
        print("Esté animal é um mamífero.")

class Voador:
    def voar(self):
        print("Esté animal pode voar")

class Murciego(Mamifero, Voador):
    def fazer_ruido(self):
        print("Fazer ruido: chirp, chirp")
        

bat = Murciego()
bat.amamentar()

bat.fazer_ruido()
