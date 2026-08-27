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

def main():
    
    crear_tabla_cuentas()
    crear_tabla_categorias()
    crear_tabla_operaciones()
    
    print("Tablas creadas correctamente")

if __name__ == "__main__":
    main()