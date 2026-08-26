from models.cuenta import Cuenta
from models.moneda import Moneda
from models.operacion import Operacion
from models.proposito_cuenta import PropositoCuenta
from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion

def main():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    cuenta_ahorro = Cuenta(
        nombre="Binance",
        moneda=Moneda.USD,
        proposito=PropositoCuenta.AHORRO,
        saldo=1000
    )
    
    compra_dolares = Operacion(
    fecha="13/08/2026",
    tipo=TipoOperacion.CONVERSION,
    categoria=None,
    descripcion="Compra de dolares",
    monto=100,
    cuenta_origen=mercado_pago,
    cuenta_destino=cuenta_ahorro,
    precio_conversion=1500,
    subtipo_conversion=TipoConversion.COMPRA
    )
    
    if compra_dolares.procesar():
        print("Compra de dolares realizada correctamente")
    else:
        print("No se pudo realizar la compra")
    
    venta_dolares = Operacion(
    fecha="13/08/2026",
    tipo=TipoOperacion.CONVERSION,
    categoria=None,
    descripcion="Venta de dolares",
    monto=100,
    cuenta_origen=cuenta_ahorro,
    cuenta_destino=mercado_pago,
    precio_conversion=1500,
    subtipo_conversion=TipoConversion.VENTA
    )
    
    if venta_dolares.procesar():
        print("Venta de dolares realizada correctamente")
    else:
        print("No se pudo realizar la venta")

if __name__ == "__main__":
    main()