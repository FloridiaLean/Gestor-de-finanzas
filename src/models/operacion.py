from models.tipo_operacion import TipoOperacion

class Operacion:
    
    def __init__(self,fecha,tipo,categoria,descripcion,monto,cuenta_origen,cuenta_destino,precio_conversion=None):
        self.fecha = fecha
        self.tipo = tipo
        self.categoria = categoria
        self.descripcion = descripcion
        self.monto = monto
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.precio_conversion = precio_conversion
    
    def procesar(self):
        
        if self.tipo == TipoOperacion.INGRESO:
            
            return self.cuenta_destino.acreditar(self.monto)
        
        if self.tipo == TipoOperacion.GASTO:
            
            return self.cuenta_origen.debitar(self.monto)
        
        if self.tipo == TipoOperacion.TRANSFERENCIA:
            
            transferencia_realizada = self.cuenta_origen.debitar(self.monto)
            
            if transferencia_realizada:
                return self.cuenta_destino.acreditar(self.monto)
            
            return False
        
        if self.tipo == TipoOperacion.COMPRA_DOLARES:
            
            monto_ars = self.monto * self.precio_conversion
            
            compra_realizada = self.cuenta_origen.debitar(monto_ars)
            
            if compra_realizada:
                    return self.cuenta_destino.acreditar(self.monto) 
                
            return False
        
        if self.tipo == TipoOperacion.VENTA_DOLARES:
            
            monto_ars = self.monto * self.precio_conversion
            
            venta_realizada = self.cuenta_origen.debitar(self.monto)
            
            if venta_realizada:
                return self.cuenta_destino.acreditar(monto_ars)
            
            return False
        
        return False
