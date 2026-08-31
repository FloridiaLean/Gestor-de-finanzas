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
from database.categorias import (
    guardar_categoria,
    obtener_categoria,
    actualizar_categoria
)
from database.operaciones import (
    guardar_operacion,
    obtener_operacion,
    actualizar_operacion,
    obtener_operaciones,
    obtener_operaciones_por_periodo,
    obtener_operaciones_por_categoria,
    obtener_operaciones_por_tipo,
    obtener_operaciones_por_cuenta
)

def main():
    
    conexion = obtener_conexion()
    
    operaciones = obtener_operaciones_por_cuenta(1,conexion)
    
    for operacion in operaciones:
        print(operacion.id,operacion.fecha,operacion.tipo,operacion.descripcion,operacion.monto)
    
    conexion.close()

if __name__ == "__main__":
    main()