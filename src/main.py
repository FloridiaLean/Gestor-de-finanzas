from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta


def main():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=180000
    )
    
    print(f"Saldo inicial: {mercado_pago.saldo}")
    
    mercado_pago.acreditar(50000)
    
    print(f"Saldo después del ingreso: {mercado_pago.saldo}")
    
    if mercado_pago.debitar(300000):
        print("Débito realizado correctamente")
    else:
        print("Saldo insuficiente")

    print(f"Saldo final: {mercado_pago.saldo}")



if __name__ == "__main__":
    main()