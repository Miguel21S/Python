
class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __str__(self):
        return f"Nome: {self.nome}, Cor: {self.cor}, Acordado: {self.acordado}"
        
    def latir(self):
        print("Auuuu...") 

    def dormir(self):
        self.acordado = False
        print("Zzzzzz, ...")

