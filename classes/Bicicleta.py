
class Bicicleta:
    def __init__(self, cor, modelo, ano, precio):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.precio = precio
        self.velocidad = 0 
        
    def __str__(self):
        return f"Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Precio: {self.precio}"

    def buzinar(self):
        print("pinnn...")

    def parar(self, velocidad = 0):
        self.velocidad = velocidad
        
        self.velocidad -= velocidad
        return f"Velocidade = {self.velocidad}, a bicicleta está parado"
    
    def aumenta_velocidade(self, incremento = 1):
        self.velocidad += incremento
        
        return f"Velocidade actual = {self.velocidad}, a bicicleta esta em movimento"
    
    def diminuir_velocidad(self, decremento = 1):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        return f"diminuir velocidade, em {decremento} velocidade actual: {self.velocidad}"
    
    def tipos_de_velocidades(self, v_diminuir = 0, v_aumentar = 0):
        # self.velocidad = v_inicial
        
        if self.velocidad <= 0 and v_aumentar <= 0:
            return f"A bicicleta está parado"
        
        if self.velocidad > 0 and v_aumentar == 0 and v_diminuir == 0:
            return f"A bicicleta está em movimento com uma velocidade inicial de {self.velocidad}"
        
        v_diminuir = max(0, v_diminuir)
        v_aumentar = max(0, v_aumentar)
        
        self.velocidad += v_aumentar
        self.velocidad -= v_diminuir

        self.velocidad = max(0, self.velocidad)
        
        return f"\nSe diminui: {v_diminuir}\nSe aumento: {v_aumentar}\nVelocidade actual: {self.velocidad}"
                