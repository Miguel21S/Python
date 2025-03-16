
class Motor:
    def __init__(self, tipo_de_motor):
        self.tipo_de_motor = tipo_de_motor
        
    def mostrar_motor(self):
        print(f"\tInformação de motor: {self.tipo_de_motor}")