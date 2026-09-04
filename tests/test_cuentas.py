from database.database import obtener_conexion
from database.cuentas import (
    guardar_cuenta,
    obtener_cuenta,
    actualizar_cuenta,
    obtener_cuentas
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
    
    guardar_cuenta(cuenta,conexion)
    
    resultado = conexion.execute("""
        SELECT id,nombre,moneda,proposito,saldo
        FROM cuentas
        WHERE id = ?
    """, (cuenta.id,)).fetchone()
    
    assert cuenta.id is not None
    assert isinstance(cuenta.id,int)
    assert resultado is not None
    assert resultado[0] == cuenta.id
    assert resultado[1] == "Mercado Pago"
    assert resultado[2] == "ARS"
    assert resultado[3] == "DISPONIBLE"
    assert resultado[4] == 200000
    
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
    assert cuenta_obtenida.id == 1
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

def test_obtener_cuentas():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    
    cuenta_1 = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=180000
    )
    
    cuenta_2 = Cuenta(
        nombre="Efectivo",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=50000
    )
    
    guardar_cuenta(cuenta_1,conexion)
    guardar_cuenta(cuenta_2,conexion)
    
    cuentas = obtener_cuentas(conexion)
    
    assert len(cuentas) == 2
    assert isinstance(cuentas[0], Cuenta)
    assert cuentas[0].nombre == "Mercado Pago"
    assert cuentas[0].moneda == Moneda.ARS
    assert cuentas[0].proposito == PropositoCuenta.DISPONIBLE
    assert cuentas[0].saldo == 180000
    assert isinstance(cuentas[1], Cuenta)
    assert cuentas[1].nombre == "Efectivo"
    assert cuentas[1].moneda == Moneda.ARS
    assert cuentas[1].proposito == PropositoCuenta.DISPONIBLE
    assert cuentas[1].saldo == 50000
    
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
    
    assert cuenta_obtenida is not None
    assert cuenta_obtenida.id == 1
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