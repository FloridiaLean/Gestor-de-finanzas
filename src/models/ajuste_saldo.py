class AjusteSaldo:
    
    def __init__(self,cuenta,fecha,saldo_anterior,saldo_nuevo,motivo,id=None):
        
        self.cuenta = cuenta
        self.fecha = fecha
        self.saldo_anterior = saldo_anterior
        self.saldo_nuevo = saldo_nuevo
        self.motivo = motivo
        self.id = id