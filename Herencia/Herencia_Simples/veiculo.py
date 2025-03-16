
class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas
        
    def __str__(self):
        return f"{__class__.__name__}\n{[f'{chave}: {valor}' for chave, valor in self.__dict__.items()]}"
