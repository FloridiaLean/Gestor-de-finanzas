from models.tipo_operacion import TipoOperacion

class Operacion:
    
    def __init__(self,fecha,tipo,categoria,descripcion,monto,cuenta):
        self.fecha = fecha
        self.tipo = tipo
        self.categoria = categoria
        self.descripcion = descripcion
        self.monto = monto
        self.cuenta = cuenta
    
    def procesar(self):
        
        if self.tipo == TipoOperacion.INGRESO:
            return self.cuenta.acreditar(self.monto)
        
        if self.tipo == TipoOperacion.GASTO:
            return self.cuenta.debitar(self.monto)
        
        return False
