from models.cuenta import Cuenta
from models.moneda import Moneda
from models.operacion import Operacion
from models.proposito_cuenta import PropositoCuenta
from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion
from models.categoria import Categoria

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
    
    categoria = Categoria("Comida")
    
    print(categoria.nombre)
    print(categoria.activa)

if __name__ == "__main__":
    main()