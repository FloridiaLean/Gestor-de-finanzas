from database.database import obtener_conexion
from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta

def guardar_cuenta(cuenta,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    conexion.execute("""
        INSERT INTO cuentas (nombre,moneda,proposito,saldo)
        VALUES (?,?,?,?)
    """, (
        cuenta.nombre,
        cuenta.moneda.value,
        cuenta.proposito.value,
        cuenta.saldo
    ))
    
    conexion.commit()
    
    if conexion_propia:
        conexion.close()

def obtener_cuenta(id_cuenta,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultado = conexion.execute("""
        SELECT nombre,moneda,proposito,saldo
        FROM cuentas
        WHERE id = ?
    """, (id_cuenta,)).fetchone()
    
    if conexion_propia:
        conexion.close()
    
    if resultado is None:
        return None
    
    return Cuenta(
        nombre=resultado[0],
        moneda=Moneda(resultado[1]),
        proposito=PropositoCuenta(resultado[2]),
        saldo=resultado[3]
    )

def actualizar_cuenta(id_cuenta,cuenta,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultado = conexion.execute("""
        UPDATE cuentas
        SET nombre = ?,
            moneda = ?,
            proposito = ?,
            saldo = ?
        WHERE id = ?
    """, (
        cuenta.nombre,
        cuenta.moneda.value,
        cuenta.proposito.value,
        cuenta.saldo,
        id_cuenta
    ))
    
    conexion.commit()
    
    actualizada = resultado.rowcount > 0
    
    if conexion_propia:
        conexion.close()
    
    return actualizada