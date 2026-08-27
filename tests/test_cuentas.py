from database.database import obtener_conexion
from database.cuentas import (
    guardar_cuenta,
    obtener_cuenta,
    actualizar_cuenta
)
from database.schema import crear_tabla_cuentas
from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta


def test_guardar_cuenta():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    ) 
    
    guardar_cuenta(cuenta)
    
    conexion = obtener_conexion()
    
    resultado = conexion.execute("""
        SELECT nombre,moneda,proposito,saldo
        FROM cuentas
        WHERE nombre = ?
    """, ("Mercado Pago",)).fetchone()
    
    assert resultado is not None
    assert resultado[0] == "Mercado Pago"
    assert resultado[1] == "ARS"
    assert resultado[2] == "DISPONIBLE"
    assert resultado[3] == 200000
    
    conexion.close()

def test_obtener_cuenta_existente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    ) 
    
    guardar_cuenta(cuenta,conexion)
    
    cuenta_obtenida = obtener_cuenta(1,conexion)
    
    assert cuenta_obtenida is not None
    assert cuenta_obtenida.nombre == "Mercado Pago"
    assert cuenta_obtenida.moneda == Moneda.ARS
    assert cuenta_obtenida.proposito == PropositoCuenta.DISPONIBLE
    assert cuenta_obtenida.saldo == 200000
    
    conexion.close()

def test_obtener_cuenta_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    
    cuenta_obtenida = obtener_cuenta(999,conexion)
    
    assert cuenta_obtenida is None
    
    conexion.close()

def test_actualizar_cuenta():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    guardar_cuenta(cuenta,conexion)
    
    cuenta_actualizada = Cuenta(
        nombre="Mercado Pago Personal",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=250000
    )
    
    resultado = actualizar_cuenta(1,cuenta_actualizada,conexion)
    
    assert resultado is True
    
    cuenta_obtenida = obtener_cuenta(1,conexion)
    
    assert cuenta_obtenida.nombre == "Mercado Pago Personal"
    assert cuenta_obtenida.moneda == Moneda.ARS
    assert cuenta_obtenida.proposito == PropositoCuenta.DISPONIBLE
    assert cuenta_obtenida.saldo == 250000
    
    conexion.close()

def test_actualizar_cuenta_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    resultado = actualizar_cuenta(999,cuenta,conexion)
    
    assert resultado is False
    
    conexion.close()