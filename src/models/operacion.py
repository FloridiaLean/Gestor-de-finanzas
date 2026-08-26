from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion
from models.moneda import Moneda
from models.categoria import Categoria
from models.proposito_cuenta import PropositoCuenta

class Operacion:
    
    def __init__(self,fecha,tipo,categoria,descripcion,monto,cuenta_origen,cuenta_destino,precio_conversion=None,subtipo_conversion=None):
        self.fecha = fecha
        self.tipo = tipo
        self.categoria = categoria
        self.descripcion = descripcion
        self.monto = monto
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.precio_conversion = precio_conversion
        self.subtipo_conversion = subtipo_conversion
    
    def validar_categoria(self):
        
        if self.categoria is None:
            return False
        
        if not self.categoria.activa:
            return False
        
        return True

    def calcular_monto_ars(self):
        
        return self.monto * self.precio_conversion
    
    def validar_monedas_conversion(self):
            
            if self.subtipo_conversion == TipoConversion.COMPRA:
                return (self.cuenta_origen.moneda == Moneda.ARS and self.cuenta_destino.moneda == Moneda.USD)
            
            if self.subtipo_conversion == TipoConversion.VENTA:
                return (self.cuenta_origen.moneda == Moneda.USD and self.cuenta_destino.moneda == Moneda.ARS)
            return False

    def validar_proposito_conversion(self):
    
        if self.subtipo_conversion == TipoConversion.COMPRA:
            return (self.cuenta_origen.proposito == PropositoCuenta.DISPONIBLE and self.cuenta_destino.proposito == PropositoCuenta.AHORRO)
        
        if self.subtipo_conversion == TipoConversion.VENTA:
            return (self.cuenta_origen.proposito == PropositoCuenta.AHORRO and self.cuenta_destino.proposito == PropositoCuenta.DISPONIBLE)
        
        return False

    def validar_conversion(self):
        
        if self.monto <= 0:
            return False
        
        if self.precio_conversion is None or self.precio_conversion <= 0:
            return False
        
        if self.cuenta_origen is None:
            return False
        
        if self.cuenta_destino is None:
            return False
        
        if self.subtipo_conversion is None:
            return False
        
        if not self.validar_monedas_conversion():
            return False
        
        if not self.validar_proposito_conversion():
                    return False
        
        return True

    def procesar(self):
        
        if self.tipo == TipoOperacion.INGRESO:
            
            if not self.validar_categoria():
                return False
            
            return self.cuenta_destino.acreditar(self.monto)
        
        if self.tipo == TipoOperacion.GASTO:
            
            if not self.validar_categoria():
                return False
            
            return self.cuenta_origen.debitar(self.monto)
        
        if self.tipo == TipoOperacion.TRANSFERENCIA:
            
            transferencia_realizada = self.cuenta_origen.debitar(self.monto)
            
            if transferencia_realizada:
                return self.cuenta_destino.acreditar(self.monto)
            return False
        
        if self.tipo == TipoOperacion.CONVERSION:
            
            if not self.validar_conversion():
                return False
            
            monto_ars = self.calcular_monto_ars()
            
            if self.subtipo_conversion == TipoConversion.COMPRA:
                
                compra_realizada = self.cuenta_origen.debitar(monto_ars)
                
                if compra_realizada:
                    return self.cuenta_destino.acreditar(self.monto) 
                return False
            
            if self.subtipo_conversion == TipoConversion.VENTA: 
            
                venta_realizada = self.cuenta_origen.debitar(self.monto)
                
                if venta_realizada:
                    return self.cuenta_destino.acreditar(monto_ars)
            return False
        
        return False
