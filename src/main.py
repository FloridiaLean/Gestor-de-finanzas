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
    
    print(f"Saldo inicial: {mercado_pago.saldo}")
    
    gasto_hamburguesa = Operacion(
        fecha="13/08/2026",
        tipo=TipoOperacion.GASTO,
        categoria="Comida",
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=mercado_pago,
        cuenta_destino=None
    )
    
    if gasto_hamburguesa.procesar():
        print("Operación procesada correctamente")
    else:
        print("No se pudo procesar la operación")
    
    print(f"Saldo 1ra operación: {mercado_pago.saldo}")
    
    
    cobro_quincena = Operacion(
        fecha="13/08/2026",
        tipo=TipoOperacion.INGRESO,
        categoria="INGRESO",
        descripcion="COBROQUINCENA",
        monto=200000,
        cuenta_origen=None,
        cuenta_destino=mercado_pago
    )
    
    if cobro_quincena.procesar():
            print("2da operación procesada correctamente")
    else:
        print("No se pudo procesar la operación")
        
    print(f"Saldo final: {mercado_pago.saldo}")

if __name__ == "__main__":
    main()