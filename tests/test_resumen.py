from database.database import obtener_conexion
from database.schema import (
    crear_tabla_cuentas,
    crear_tabla_categorias,
    crear_tabla_operaciones
)
from database.categorias import (
    guardar_categoria,
    actualizar_categoria
)
from consultas.resumen import obtener_resumen_anual
from database.cuentas import guardar_cuenta
from database.operaciones import guardar_operacion
from models.categoria import Categoria
from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta
from models.operacion import Operacion
from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion


def test_resumen_anual_contiene_doce_meses():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    resumen = obtener_resumen_anual(2026,conexion=conexion)
    
    assert resumen["año"] == 2026
    assert len(resumen["meses"]) == 12
    
    assert resumen["meses"][0]["nombre"] == "Enero"
    assert resumen["meses"][7]["nombre"] == "Agosto"
    assert resumen["meses"][11]["nombre"] == "Diciembre"
    
    conexion.close()

def test_resumen_gastos_por_categoria():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=500000
    )
    
    guardar_cuenta(cuenta, conexion)
    
    comida = Categoria("Comida")
    transporte = Categoria("Transporte")
    
    guardar_categoria(comida,conexion)
    guardar_categoria(transporte,conexion)
    
    gasto_1 = Operacion(
        fecha="2026-08-10",
        tipo=TipoOperacion.GASTO,
        categoria=comida,
        descripcion="Cena",
        monto=18000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    gasto_2 = Operacion(
        fecha="2026-08-20",
        tipo=TipoOperacion.GASTO,
        categoria=comida,
        descripcion="Supermercado",
        monto=200000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    ) 
    
    gasto_3 = Operacion(
        fecha="2026-09-05",
        tipo=TipoOperacion.GASTO,
        categoria=transporte,
        descripcion="Taxi",
        monto=15000,
        cuenta_origen=cuenta,
        cuenta_destino=None
    )
    
    guardar_operacion(gasto_1,conexion)
    guardar_operacion(gasto_2,conexion)
    guardar_operacion(gasto_3,conexion)
    
    resumen = obtener_resumen_anual(2026,conexion)
    
    agosto = resumen["meses"][7]
    septiembre = resumen["meses"][8]
    
    assert agosto["gastos"] == 218000
    assert agosto["gastos_por_categoria"]["Comida"] == 218000
    assert agosto["gastos_por_categoria"]["Transporte"] == 0
    assert septiembre["gastos"] == 15000
    assert septiembre["gastos_por_categoria"]["Comida"] == 0
    assert septiembre["gastos_por_categoria"]["Transporte"] == 15000
    
    conexion.close()

def test_resumen_ingresos_transferencias_y_años():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta_origen = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=500000
    )
    
    cuenta_destino = Cuenta(
        nombre="Efectivo",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=50000
    )
    
    guardar_cuenta(cuenta_origen,conexion)
    guardar_cuenta(cuenta_destino,conexion)
    
    categoria_ingreso = Categoria("Ingreso")
    categoria_comida = Categoria("Comida")
    
    guardar_categoria(categoria_ingreso,conexion)
    guardar_categoria(categoria_comida,conexion)
    
    ingreso = Operacion(
        fecha="2026-08-01",
        tipo=TipoOperacion.INGRESO,
        categoria=categoria_ingreso,
        descripcion="Cobro quincena",
        monto=120000,
        cuenta_origen=None,
        cuenta_destino=cuenta_origen
    )
    
    gasto = Operacion(
        fecha="2026-08-05",
        tipo=TipoOperacion.GASTO,
        categoria=categoria_comida,
        descripcion="Cena",
        monto=20000,
        cuenta_origen=cuenta_origen,
        cuenta_destino=None
    )
    
    transferencia = Operacion(
        fecha="2026-08-10",
        tipo=TipoOperacion.TRANSFERENCIA,
        categoria=None,
        descripcion="Retiro de efectivo",
        monto=30000,
        cuenta_origen=cuenta_origen,
        cuenta_destino=cuenta_destino
    )
    
    ingreso_otro_año = Operacion(
        fecha="2027-08-01",
        tipo=TipoOperacion.INGRESO,
        categoria=categoria_ingreso,
        descripcion="Ingreso de otro año",
        monto=500000,
        cuenta_origen=None,
        cuenta_destino=cuenta_origen
    )
    
    guardar_operacion(ingreso,conexion)
    guardar_operacion(gasto,conexion)
    guardar_operacion(transferencia,conexion)
    guardar_operacion(ingreso_otro_año,conexion)
    
    resumen = obtener_resumen_anual(2026,conexion)
    
    agosto = resumen["meses"][7]
    
    assert agosto["ingresos"] == 120000
    assert agosto["gastos"] == 20000
    assert agosto["gastos_por_categoria"]["Comida"] == 20000
    
    conexion.close()

def test_resumen_categorias_desactivadas():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    comida = Categoria("Comida")
    transporte = Categoria("Transporte")
    
    guardar_categoria(comida,conexion)
    guardar_categoria(transporte,conexion)
    
    transporte.desactivar()
    
    actualizar_categoria(transporte.id,transporte,conexion)
    
    resumen = obtener_resumen_anual(2026,conexion)
    
    assert len(resumen["meses"]) == 12
    
    for mes in resumen["meses"]:
        assert "Comida" in mes["gastos_por_categoria"]
        assert "Transporte" in mes["gastos_por_categoria"]
        assert mes["gastos_por_categoria"]["Comida"] == 0
        assert mes["gastos_por_categoria"]["Transporte"] == 0
        
    conexion.close()

def test_resumen_conversiones():
    conexion = obtener_conexion(":memory:")
    crear_tabla_cuentas(conexion)
    crear_tabla_categorias(conexion)
    crear_tabla_operaciones(conexion)
    
    cuenta_ars = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=500000
    )
    
    cuenta_usd = Cuenta(
        nombre="Dólares",
        moneda=Moneda.USD,
        proposito=PropositoCuenta.AHORRO,
        saldo=1000
    )
    
    guardar_cuenta(cuenta_ars,conexion)
    guardar_cuenta(cuenta_usd,conexion)
    
    compra = Operacion(
        fecha="2026-08-10",
        tipo=TipoOperacion.CONVERSION,
        categoria=None,
        descripcion="Compra de dólares",
        monto=200,
        cuenta_origen=cuenta_ars,
        cuenta_destino=cuenta_usd,
        precio_conversion=1500,
        subtipo_conversion=TipoConversion.COMPRA
    )
    
    venta = Operacion(
        fecha="2026-08-20",
        tipo=TipoOperacion.CONVERSION,
        categoria=None,
        descripcion="Venta de dólares",
        monto=50,
        cuenta_origen=cuenta_usd,
        cuenta_destino=cuenta_ars,
        precio_conversion=1500,
        subtipo_conversion=TipoConversion.VENTA
    )
    
    guardar_operacion(compra,conexion)
    guardar_operacion(venta,conexion)
    
    resumen = obtener_resumen_anual(2026,conexion)
    agosto = resumen["meses"][7]
    
    assert agosto["dolares_comprados"] == 200
    assert agosto["dolares_vendidos"] == 50
    assert agosto["ingresos"] == 0
    assert agosto["gastos"] == 0
    
    conexion.close()