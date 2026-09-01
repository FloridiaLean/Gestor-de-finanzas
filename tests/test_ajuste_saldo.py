from database.database import obtener_conexion
from database.ajustes_saldo import (
    guardar_ajuste_saldo,
    obtener_ajuste_saldo,
    ajustar_saldo
)
from database.cuentas import (
    guardar_cuenta,
    obtener_cuenta
)
from models.ajuste_saldo import AjusteSaldo
from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta
from database.schema import (
    crear_tabla_cuentas,
    crear_tabla_ajustes_saldo
)

def test_crear_ajuste_saldo():
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=230000
    )
    
    ajuste = AjusteSaldo(
        cuenta=cuenta,
        fecha="2026-08-31",
        saldo_anterior=230000,
        saldo_nuevo=232500,
        motivo="Rendimientos acumulados"
    )
    
    assert ajuste.id is None
    assert ajuste.cuenta is cuenta
    assert ajuste.fecha == "2026-08-31"
    assert ajuste.saldo_anterior == 230000
    assert ajuste.saldo_nuevo == 232500
    assert ajuste.motivo == "Rendimientos acumulados"

def test_guardar_ajuste_saldo():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_ajustes_saldo(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=230000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    ajuste = AjusteSaldo(
        cuenta=cuenta,
        fecha="2026-08-31",
        saldo_anterior=230000,
        saldo_nuevo=232500,
        motivo="Rendimientos acumulados"
    )
    
    guardar_ajuste_saldo(ajuste,conexion)
    
    resultado = conexion.execute("""
        SELECT
            id,
            cuenta_id,
            fecha,
            saldo_anterior,
            saldo_nuevo,
            motivo
        FROM ajustes_saldo
        WHERE id = ?
    """, (ajuste.id,)).fetchone()
    
    assert ajuste.id is not None
    assert isinstance(ajuste.id, int)
    assert resultado is not None
    assert resultado[0] == ajuste.id
    assert resultado[1] == cuenta.id
    assert resultado[2] == "2026-08-31"
    assert resultado[3] == 230000
    assert resultado[4] == 232500
    assert resultado[5] == "Rendimientos acumulados"
    
    conexion.close()

def test_obtener_ajuste_saldo_existente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_ajustes_saldo(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=230000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    ajuste = AjusteSaldo(
        cuenta=cuenta,
        fecha="2026-08-31",
        saldo_anterior=230000,
        saldo_nuevo=232500,
        motivo="Rendimientos acumulados"
    )
    
    guardar_ajuste_saldo(ajuste,conexion)
    
    ajuste_obtenido = obtener_ajuste_saldo(ajuste.id,conexion)
    
    assert ajuste_obtenido is not None
    assert ajuste_obtenido.id == ajuste.id
    assert ajuste_obtenido.cuenta.id == cuenta.id
    assert ajuste_obtenido.fecha == "2026-08-31"
    assert ajuste_obtenido.saldo_anterior == 230000
    assert ajuste_obtenido.saldo_nuevo == 232500
    assert ajuste_obtenido.motivo == "Rendimientos acumulados"
    
    conexion.close()

def test_obtener_ajuste_saldo_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_ajustes_saldo(conexion)
    
    ajuste = obtener_ajuste_saldo(999,conexion)
    
    assert ajuste is None
    
    conexion.close()

def test_ajustar_saldo():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_ajustes_saldo(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=230000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    ajuste = ajustar_saldo(
        cuenta=cuenta,
        nuevo_saldo=232500,
        fecha="2026-08-31",
        motivo="Rendimientos acumulados",
        conexion=conexion
    )
    
    assert ajuste is not None
    assert ajuste.id is not None
    assert isinstance(ajuste.id,int)
    assert ajuste.cuenta is cuenta
    assert ajuste.saldo_anterior == 230000
    assert ajuste.saldo_nuevo == 232500
    assert ajuste.motivo == "Rendimientos acumulados"
    assert cuenta.saldo == 232500
    
    cuenta_obtenida = obtener_cuenta(cuenta.id,conexion)
    
    assert cuenta_obtenida.saldo == 232500
    
    ajuste_obtenido = obtener_ajuste_saldo(ajuste.id,conexion)
    
    assert ajuste_obtenido is not None
    assert ajuste_obtenido.id == ajuste.id
    assert ajuste_obtenido.cuenta.id == cuenta.id
    assert ajuste_obtenido.saldo_anterior == 230000
    assert ajuste_obtenido.saldo_nuevo == 232500
    
    conexion.close()

def test_ajustar_saldo_utiliza_saldo_actual():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_ajustes_saldo(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=230000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    primer_ajuste = ajustar_saldo(
        cuenta=cuenta,
        nuevo_saldo=232500,
        fecha="2026-08-31",
        motivo="Primer ajuste",
        conexion=conexion
    )
    
    segundo_ajuste = ajustar_saldo(
        cuenta=cuenta,
        nuevo_saldo=240000,
        fecha="2026-09-01",
        motivo="Segundo ajuste",
        conexion=conexion
    )
    
    assert primer_ajuste.saldo_anterior == 230000
    assert primer_ajuste.saldo_nuevo == 232500
    assert segundo_ajuste.saldo_anterior == 232500
    assert segundo_ajuste.saldo_nuevo == 240000
    assert cuenta.saldo == 240000
    
    conexion.close()

