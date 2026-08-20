from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta

class Cuenta:
    
    def __init__(self,nombre,moneda,proposito,saldo):
        self.nombre = nombre
        self.moneda = moneda
        self.proposito = proposito
        self.saldo = saldo
    
    def acreditar(self,monto):
        
        if monto <= 0:
            return False
        
        self.saldo += monto
        return True
    
    def debitar(self,monto):
        
        if monto <= 0:
            return False
        
        if monto > self.saldo:
            return False
        
        self.saldo -= monto
        return True
    
    def __str__(self):
        return (
            f"Cuenta: {self.nombre}\n"
            f"Moneda: {self.moneda.value}\n"
            f"Propósito: {self.proposito.value}\n"
            f"Saldo: {self.saldo}"
        )