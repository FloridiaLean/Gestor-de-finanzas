from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta
from models.tipo_operacion import TipoOperacion
from models.operacion import Operacion

def main():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    efectivo = Cuenta(
    nombre="Efectivo",
    moneda=Moneda.ARS,
    proposito=PropositoCuenta.DISPONIBLE,
    saldo=50000
    )
    cuenta_ahorro = Cuenta(
        nombre="Binance",
        moneda=Moneda.USD,
        proposito=PropositoCuenta.AHORRO,
        saldo=1000
    )
    
    compra_dolares = Operacion(
    fecha="13/08/2026",
    tipo=TipoOperacion.COMPRA_DOLARES,
    categoria=None,
    descripcion="Compra de dólares",
    monto=100,
    cuenta_origen=mercado_pago,
    cuenta_destino=cuenta_ahorro,
    precio_conversion=1500
    )
    
    print(f"Mercado Pago antes: ${mercado_pago.saldo}")
    print(f"Ahorro antes: USD {cuenta_ahorro.saldo}")
    
    if compra_dolares.procesar():
        print("Compra de dólares realizada correctamente")
    else:
        print("No se pudo realizar la compra")
    
    print(f"Mercado Pago después: ${mercado_pago.saldo}")
    print(f"Ahorro después: USD {cuenta_ahorro.saldo}") 
    print("")
    
    venta_dolares = Operacion(
    fecha="13/08/2026",
    tipo=TipoOperacion.VENTA_DOLARES,
    categoria=None,
    descripcion="Venta de dólares",
    monto=100,
    cuenta_origen=cuenta_ahorro,
    cuenta_destino=mercado_pago,
    precio_conversion=1500
    )
    
    print(f"Mercado Pago antes: ${mercado_pago.saldo}")
    print(f"Ahorro antes: USD {cuenta_ahorro.saldo}")
    
    if venta_dolares.procesar():
        print("Venta de dólares realizada correctamente")
    else:
        print("No se pudo realizar la venta")
    
    print(f"Mercado Pago después: ${mercado_pago.saldo}")
    print(f"Ahorro después: USD {cuenta_ahorro.saldo}")
    
if __name__ == "__main__":
    main()