import veiculo

class Mota(veiculo.Veiculo):
    def __init__(self, marca, modelo, tipo_de_motor, cilindrada):
        super().__init__(marca, modelo)
        
        self.tipo_de_motor = tipo_de_motor
        self.cilindrada = cilindrada
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"\tTipo de motor: {self.tipo_de_motor}")
        print(f"\tCilindrada: {self.cilindrada} cc")