import veiculo, motor

class Carro(veiculo.Veiculo, motor.Motor):
    def __init__(self, marca, modelo, tipo_de_motor, portas):
        veiculo.Veiculo.__init__(self, marca, modelo)
        motor.Motor.__init__(self, tipo_de_motor)
        
        self.portas = portas
        
    def mostrar_info(self):
        super().mostrar_info()
        super().mostrar_motor()
        print(f"\tNúmero de portas: {self.portas}")
    
    