from models.cuenta import Cuenta
from models.moneda import Moneda
from models.operacion import Operacion
from models.proposito_cuenta import PropositoCuenta
from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion
from models.categoria import Categoria
from database.database import obtener_conexion
from database.schema import (
    crear_tabla_ajustes_saldo,
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
from database.ajustes_saldo import ajustar_saldo

def main():
    
    conexion = obtener_conexion()
    
    cuenta = obtener_cuenta(1)
    
    print("Saldo actual:", cuenta.saldo)
    
    ajuste = ajustar_saldo(
        cuenta=cuenta,
        nuevo_saldo=250000,
        fecha="2026-09-01",
        motivo="Corrección de saldo"
    )
    
    print("Nuevo saldo:", cuenta.saldo)
    print("ID del ajuste:", ajuste.id)
    print("Saldo anterior:", ajuste.saldo_anterior)
    print("Saldo nuevo:", ajuste.saldo_nuevo)
    print("Motivo:", ajuste.motivo)
    
    cuenta_bd = obtener_cuenta(cuenta.id)
    
    print("Saldo guardado en BD:", cuenta_bd.saldo)
    
    ajuste_2 = ajustar_saldo(
    cuenta=cuenta,
    nuevo_saldo=275000,
    fecha="2026-09-01",
    motivo="Segundo ajuste de prueba"
    )
    
    print("Saldo actual:", cuenta.saldo)
    print("ID ajuste:", ajuste_2.id)
    print("Saldo anterior:", ajuste_2.saldo_anterior)
    print("Saldo nuevo:", ajuste_2.saldo_nuevo)
    print("Motivo:", ajuste_2.motivo)
    
    conexion.close()

if __name__ == "__main__":
    main()