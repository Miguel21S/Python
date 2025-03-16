
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def mostrar_info(self):
        print(f"\tVeiculo: {self.marca}, {self.modelo}")