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
    obtener_operaciones
)

def main():
    
    conexion = obtener_conexion()
    
    categoria = obtener_categoria(1,conexion)
    cuenta = obtener_cuenta(1,conexion)
    
    operacion_actualizada = Operacion(
        fecha = "30/8/2026",
        tipo = TipoOperacion.GASTO,
        categoria = categoria,
        descripcion = "Pollo con papas",
        monto = 12000,
        cuenta_origen = cuenta,
        cuenta_destino = None
    )
    
    resultado = actualizar_operacion(4,operacion_actualizada,conexion)
    
    operaciones = obtener_operaciones(conexion)
    
    print(f"Cantidad de operaciones: {len(operaciones)}")
    
    for operacion in operaciones:
        print("--------------------")
        print("ID:", operacion.id)
        print("Fecha:", operacion.fecha)
        print("Tipo:", operacion.tipo.value)
        print("Descripcion:", operacion.descripcion)
        print("Monto:", operacion.monto)
        
        if operacion.categoria is not None:
            print("Categoria:", operacion.categoria.nombre)
        
        if operacion.cuenta_origen is not None:
            print("Cuenta origen:", operacion.cuenta_origen.nombre)
        
        if operacion.cuenta_destino is not None:
            print("Cuenta destino:", operacion.cuenta_destino.nombre)
        
    conexion.close()

if __name__ == "__main__":
    main()