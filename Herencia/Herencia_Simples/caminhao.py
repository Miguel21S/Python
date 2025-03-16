import veiculo

class Caminhao(veiculo.Veiculo):
    def __init__(self, cor, placa, n_rodas, carregado = True):
        super().__init__(cor, placa, n_rodas)
        self.carregado = carregado
        
    def __str__(self):
        return super().__str__()
    
    def esta_carregado(self):
        print(f"{'Caminhão está carregado' if self.carregado else 'Caminhão não está carregado'}")
    