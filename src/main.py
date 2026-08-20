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
    
    print(f"Saldo despues de 1ra operación: {mercado_pago.saldo}")
    
    
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
        
    print(f"Saldo despues de 2da operación: {mercado_pago.saldo}")
    
    print(f"Mercado Pago saldo: {mercado_pago.saldo}")
    print(f"Efectivo antes: {efectivo.saldo}")
    
    transferencia_efectivo = Operacion(
    fecha="13/08/2026",
    tipo=TipoOperacion.TRANSFERENCIA,
    categoria=None,
    descripcion="Retiro de efectivo",
    monto=30000,
    cuenta_origen=mercado_pago,
    cuenta_destino=efectivo
    )
    
    if transferencia_efectivo.procesar():
        print("Transferencia realizada correctamente")
    else:
        print("No se pudo realizar la transferencia")
    
    print(f"Mercado Pago después: {mercado_pago.saldo}")
    print(f"Efectivo después: {efectivo.saldo}")
    
if __name__ == "__main__":
    main()