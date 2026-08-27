from models.cuenta import Cuenta
from models.moneda import Moneda
from models.operacion import Operacion
from models.proposito_cuenta import PropositoCuenta
from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion
from models.categoria import Categoria
from database.database import obtener_conexion
from database.schema import (
    crear_tabla_cuentas,
    crear_tabla_categorias,
    crear_tabla_operaciones
)
from database.cuentas import (
    guardar_cuenta,
    obtener_cuenta,
    actualizar_cuenta
)

def main():
    
    cuenta = obtener_cuenta(2)
    
    print("ANTES:")
    print(cuenta)
    
    cuenta_actualizada = Cuenta(
        nombre="Efectivo fisico",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=75000
    )
    
    resultado = actualizar_cuenta(2, cuenta_actualizada)
    
    if resultado:
        print("\nCuenta actualizada correctamente")
    else:
        print("\nNo se encontro la cuenta")
    
    cuenta = obtener_cuenta(2)
    
    print("\nDESPUES:")
    print(cuenta)

if __name__ == "__main__":
    main()