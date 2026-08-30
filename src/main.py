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
    actualizar_operacion
)

def main():
    
    conexion = obtener_conexion()
    
    operacion = obtener_operacion(2,conexion)
    
    if operacion is not None:
    
        print("Operación original:")
        print("ID:", operacion.id)
        print("Descripción:", operacion.descripcion)
        print("Monto:", operacion.monto)
        print("Categoría:", operacion.categoria.nombre)
    
    categoria = obtener_categoria(1, conexion)
    cuenta = obtener_cuenta(1, conexion)
    
    operacion_actualizada = Operacion(
        fecha=operacion.fecha,
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Cena",
        monto=18000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    resultado = actualizar_operacion(operacion.id,operacion_actualizada,conexion)
    
    print("\nResultado de actualización:", resultado)
    
    operacion_obtenida = obtener_operacion(operacion.id,conexion)
    
    print("\nOperación actualizada:")
    print("ID:", operacion_obtenida.id)
    print("Descripción:", operacion_obtenida.descripcion)
    print("Monto:", operacion_obtenida.monto)
    print("Categoría:", operacion_obtenida.categoria.nombre)
    print("Cuenta origen:", operacion_obtenida.cuenta_origen.nombre)
    
    conexion.close()

if __name__ == "__main__":
    main()