
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
    
    def __str__(self):
        return f"Datos de la cuenta,\nNombre: {self._titular}\nSaldo: {self._saldo}"
        
    @property
    def saldo(self):
        if self._saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        else:
            return self._saldo
    
    def depositar(self, saldo):
        self._saldo += saldo
        return f"Depósito de {saldo}: Saldo actual {self._saldo}"

    def retirar(self, saldo):
        if self._saldo < saldo:
            raise ValueError(f"Intento de retirar {saldo}: Saldo insuficiente")
        self._saldo -= saldo
        return f"Retirada de {saldo}: Saldo actual {self._saldo}"
    

banco = CuentaBancaria("Miguel", 1000)
print(banco)

print(banco.depositar(500))
print(banco.retirar(2000))