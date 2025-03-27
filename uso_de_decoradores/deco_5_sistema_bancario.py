""" 
Ejercicio 5: @property con validación
Objetivo:
Crear una clase CuentaBancaria que tenga:

Atributos: titular, saldo.

Un @property llamado saldo que solo permita valores positivos.

Métodos depositar() y retirar() para modificar el saldo.

📝 Instrucciones:
Valida que el saldo nunca sea negativo.

Muestra un mensaje si se intenta retirar más dinero del que hay disponible.

💡 Salida esperada:
        Saldo actual: 1000
        Depósito de 500: Nuevo saldo: 1500
        Intento de retirar 2000: Saldo insuficiente
"""

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

try:
    print(banco.depositar(500))
    print(banco.retirar(2000))
except ValueError as e:
    print(e)