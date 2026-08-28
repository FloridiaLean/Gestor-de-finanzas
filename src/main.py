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

def main():
    
    categoria = obtener_categoria(9)
    
    if categoria is not None:
        
        print("Estado antes:", categoria.activa)
        
        categoria.desactivar()
        
        resultado = actualizar_categoria(9,categoria)
        
        if resultado:
            print("Categoria actualizada correctamente")
            
            categoria = obtener_categoria(9)
            
            print("Estado despues:", categoria.activa)
        
    else:
        print("Categoria no encontrada")

if __name__ == "__main__":
    main()