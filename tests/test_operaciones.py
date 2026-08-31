from database.database import obtener_conexion
from database.schema import (
    crear_tabla_cuentas,
    crear_tabla_categorias,
    crear_tabla_operaciones
)
from database.cuentas import guardar_cuenta
from database.categorias import guardar_categoria
from database.operaciones import (
    guardar_operacion,
    obtener_operacion,
    obtener_operaciones,
    obtener_operaciones_por_periodo,
    obtener_operaciones_por_categoria,
    obtener_operaciones_por_tipo,
    obtener_operaciones_por_cuenta,
    actualizar_operacion
)
from models.cuenta import Cuenta
from models.categoria import Categoria
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta
from models.operacion import Operacion
from models.tipo_operacion import TipoOperacion

def test_guardar_operacion():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )   
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_cuenta(cuenta,conexion)
    guardar_categoria(categoria,conexion)
    
    operacion = Operacion(
        fecha="2026/08/28",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion,conexion)
    
    resultado = conexion.execute("""
        SELECT
            id,
            fecha,
            tipo,
            categoria_id,
            descripcion,
            monto,
            cuenta_origen_id,
            cuenta_destino_id,
            precio_conversion,
            subtipo_conversion
        FROM operaciones
        WHERE id = ?
    """, (operacion.id,)).fetchone()
    
    assert operacion.id is not None
    assert isinstance(operacion.id,int)
    assert resultado is not None
    assert resultado[0] == operacion.id
    assert resultado[1] == "2026/08/28"
    assert resultado[2] == "Gasto"
    assert resultado[3] == categoria.id
    assert resultado[4] == "Hamburguesa"
    assert resultado[5] == 15000
    assert resultado[6] == cuenta.id
    assert resultado[7] is None
    assert resultado[8] is None
    assert resultado[9] is None
    
    conexion.close()

def test_obtener_operacion_existente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_cuenta(cuenta,conexion)
    guardar_categoria(categoria,conexion)
    
    operacion = Operacion(
        fecha="2026/08/28",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion,conexion)
    
    operacion_obtenida = obtener_operacion(operacion.id,conexion)
    
    assert operacion_obtenida is not None
    assert operacion_obtenida.id == operacion.id
    assert operacion_obtenida.fecha == "2026/08/28"
    assert operacion_obtenida.tipo == TipoOperacion.GASTO
    assert operacion_obtenida.categoria is not None
    assert operacion_obtenida.categoria.id == categoria.id
    assert operacion_obtenida.categoria.nombre == "Comida"
    assert operacion_obtenida.descripcion == "Hamburguesa"
    assert operacion_obtenida.monto == 15000
    assert operacion_obtenida.cuenta_origen is not None
    assert operacion_obtenida.cuenta_origen.id == cuenta.id
    assert operacion_obtenida.cuenta_origen.nombre == "Mercado Pago"
    assert operacion_obtenida.cuenta_destino is None
    assert operacion_obtenida.precio_conversion is None
    assert operacion_obtenida.subtipo_conversion is None
    
    conexion.close()

def test_obtener_operacion_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    operacion_obtenida = obtener_operacion(999,conexion)
    
    assert operacion_obtenida is None
    
    conexion.close()

def test_obtener_operaciones():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_categoria(categoria,conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=300000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    operacion_1 = Operacion(
        fecha="2026/08/30",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa con los chicos",
        monto=17000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    operacion_2 = Operacion(
        fecha="2026/08/30",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Supermercado",
        monto=200000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion_1,conexion)
    guardar_operacion(operacion_2,conexion)
    
    operaciones = obtener_operaciones(conexion)
    
    assert isinstance(operaciones, list)
    assert len(operaciones) == 2
    assert operaciones[0].id == operacion_1.id
    assert operaciones[0].descripcion == "Hamburguesa con los chicos"
    assert operaciones[0].monto == 17000
    assert operaciones[1].id == operacion_2.id
    assert operaciones[1].descripcion == "Supermercado"
    assert operaciones[1].monto == 200000
    assert operaciones[0].categoria.nombre == "Comida"
    assert operaciones[0].cuenta_origen.nombre == "Mercado Pago"
    
    conexion.close()

def test_actualizar_operacion():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_cuenta(cuenta,conexion)
    guardar_categoria(categoria,conexion)
    
    operacion = Operacion(
        fecha="2026/08/28",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion,conexion)
    
    operacion_actualizada = Operacion(
        fecha="2026/08/28",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Cena",
        monto=18000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    resultado = actualizar_operacion(operacion.id,operacion_actualizada,conexion)
    
    assert resultado is True
    
    operacion_obtenida = obtener_operacion(operacion.id,conexion)
    
    assert operacion_obtenida is not None
    assert operacion_obtenida.id == operacion.id
    assert operacion_obtenida.descripcion == "Cena"
    assert operacion_obtenida.monto == 18000
    assert operacion_obtenida.categoria.id == categoria.id
    assert operacion_obtenida.cuenta_origen.id == cuenta.id
    assert operacion_obtenida.cuenta_destino is None
    
    conexion.close()

def test_actualizar_operacion_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    operacion = Operacion(
        fecha="2026/08/28",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    resultado = actualizar_operacion(999,operacion,conexion)
    
    assert resultado is False
    
    conexion.close()

def test_obtener_operaciones_por_periodo():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    )
    guardar_categoria(categoria,conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    guardar_cuenta(cuenta,conexion)
    
    operacion_1 = Operacion(
        fecha="2026-08-05",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    operacion_2 = Operacion(
        fecha="2026-08-20",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Supermercado",
        monto=30000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    operacion_3 = Operacion(
        fecha="2026-09-05",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Cena",
        monto=18000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion_1,conexion)
    guardar_operacion(operacion_2,conexion)
    guardar_operacion(operacion_3,conexion)
    
    operaciones = obtener_operaciones_por_periodo("2026-08-01","2026-08-31",conexion)
    
    assert len(operaciones) == 2
    assert operaciones[0].descripcion == "Hamburguesa"
    assert operaciones[1].descripcion == "Supermercado"
    
    conexion.close()

def test_obtener_operaciones_por_periodo_invalido():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    operaciones = obtener_operaciones_por_periodo("2026-08-31","2026-08-01",conexion)
    
    assert operaciones == []
    
    conexion.close()

def test_obtener_operaciones_por_categoria():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    categoria_comida = Categoria(
        nombre="Comida"
    )
    
    categoria_transporte = Categoria(
        nombre="Transporte"
    )
    
    guardar_categoria(categoria_comida,conexion)
    guardar_categoria(categoria_transporte,conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    operacion_1 = Operacion(
        fecha="2026-08-05",
        tipo=TipoOperacion.GASTO,
        categoria=categoria_comida,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )

    operacion_2 = Operacion(
        fecha="2026-08-10",
        tipo=TipoOperacion.GASTO,
        categoria=categoria_transporte,
        descripcion="Nafta",
        monto=20000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )

    operacion_3 = Operacion(
        fecha="2026-08-20",
        tipo=TipoOperacion.GASTO,
        categoria=categoria_comida,
        descripcion="Supermercado",
        monto=30000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion_1,conexion)
    guardar_operacion(operacion_2,conexion)
    guardar_operacion(operacion_3,conexion)
    
    operaciones = obtener_operaciones_por_categoria(categoria_comida.id,conexion)
    
    assert isinstance(operaciones, list)
    assert len(operaciones) == 2
    assert operaciones[0].id == operacion_1.id
    assert operaciones[0].descripcion == "Hamburguesa"
    assert operaciones[1].id == operacion_3.id
    assert operaciones[1].descripcion == "Supermercado"
    assert operaciones[0].categoria.id == categoria_comida.id
    assert operaciones[1].categoria.id == categoria_comida.id
    
    conexion.close()

def test_obtener_operaciones_por_categoria_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    operaciones = obtener_operaciones_por_categoria(999,conexion)
    
    assert operaciones == []
    
    conexion.close()

def test_obtener_operaciones_por_tipo():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_categoria(categoria,conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    operacion_1 = Operacion(
        fecha="2026-08-05",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    operacion_2 = Operacion(
        fecha="2026-08-10",
        tipo=TipoOperacion.INGRESO,
        categoria=categoria,
        descripcion="Sueldo",
        monto=300000,
        cuenta_origen=None,
        cuenta_destino=cuenta
    )
    operacion_3 = Operacion(
        fecha="2026-08-20",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Supermercado",
        monto=30000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion_1,conexion)
    guardar_operacion(operacion_2,conexion)
    guardar_operacion(operacion_3,conexion)
    
    operaciones = obtener_operaciones_por_tipo(TipoOperacion.GASTO,conexion)
    
    assert isinstance(operaciones, list)
    assert len(operaciones) == 2
    assert operaciones[0].id == operacion_1.id
    assert operaciones[0].descripcion == "Hamburguesa"
    assert operaciones[0].tipo == TipoOperacion.GASTO
    assert operaciones[1].id == operacion_3.id
    assert operaciones[1].descripcion == "Supermercado"
    assert operaciones[1].tipo == TipoOperacion.GASTO
    
    conexion.close()

def test_obtener_operaciones_por_tipo_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    operaciones = obtener_operaciones_por_tipo(TipoOperacion.TRANSFERENCIA,conexion)
    
    assert operaciones == []
    
    conexion.close()

def test_obtener_operaciones_por_cuenta():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_categoria(categoria,conexion)
    
    cuenta_mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    cuenta_efectivo = Cuenta(
        nombre="Efectivo",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=50000
    )
    
    guardar_cuenta(cuenta_mercado_pago,conexion)
    guardar_cuenta(cuenta_efectivo,conexion)
    
    operacion_1 = Operacion(
        fecha="2026-08-05",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Hamburguesa",
        monto=15000,
        cuenta_origen=cuenta_mercado_pago,
        cuenta_destino=None
    )
    operacion_2 = Operacion(
        fecha="2026-08-10",
        tipo=TipoOperacion.INGRESO,
        categoria=categoria,
        descripcion="Sueldo",
        monto=300000,
        cuenta_origen=None,
        cuenta_destino=cuenta_mercado_pago
    )
    operacion_3 = Operacion(
        fecha="2026-08-15",
        tipo=TipoOperacion.GASTO,
        categoria=categoria,
        descripcion="Almuerzo",
        monto=10000,
        cuenta_origen=cuenta_efectivo,
        cuenta_destino=None
    )
    
    guardar_operacion(operacion_1,conexion)
    guardar_operacion(operacion_2,conexion)
    guardar_operacion(operacion_3,conexion)
    
    operaciones = obtener_operaciones_por_cuenta(cuenta_mercado_pago.id,conexion)
    
    assert isinstance(operaciones, list)
    assert len(operaciones) == 2
    assert operaciones[0].id == operacion_1.id
    assert operaciones[0].descripcion == "Hamburguesa"
    assert operaciones[1].id == operacion_2.id
    assert operaciones[1].descripcion == "Sueldo"
    
    conexion.close()

def test_obtener_operaciones_por_cuenta_sin_resultados():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    operaciones = obtener_operaciones_por_cuenta(cuenta.id,conexion)
    
    assert operaciones == []
    
    conexion.close()