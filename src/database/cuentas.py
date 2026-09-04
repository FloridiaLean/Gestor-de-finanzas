from database.database import obtener_conexion
from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta

def guardar_cuenta(cuenta,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    cursor = conexion.execute("""
        INSERT INTO cuentas (
            nombre,
            moneda,
            proposito,
            saldo
        )
        VALUES (?,?,?,?)
    """, (
        cuenta.nombre,
        cuenta.moneda.value,
        cuenta.proposito.value,
        cuenta.saldo
    ))
    
    conexion.commit()
    
    cuenta.id = cursor.lastrowid

    if conexion_propia:
        conexion.close()

def obtener_cuenta(id_cuenta,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultado = conexion.execute("""
        SELECT id,nombre,moneda,proposito,saldo
        FROM cuentas
        WHERE id = ?
    """, (id_cuenta,)).fetchone()
    
    if conexion_propia:
        conexion.close()
    
    if resultado is None:
        return None
    
    return Cuenta(
        id=resultado[0],
        nombre=resultado[1],
        moneda=Moneda(resultado[2]),
        proposito=PropositoCuenta(resultado[3]),
        saldo=resultado[4]
    )

def obtener_cuentas(conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultados = conexion.execute("""
        SELECT id,nombre,moneda,proposito,saldo
        FROM cuentas
    """).fetchall()
    
    if conexion_propia:
        conexion.close()
    
    cuentas = []
    
    for resultado in resultados:
        cuenta = Cuenta(
            id=resultado[0],
            nombre=resultado[1],
            moneda=Moneda(resultado[2]),
            proposito=PropositoCuenta(resultado[3]),
            saldo=resultado[4]
        )
        
        cuentas.append(cuenta)
    
    return cuentas

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
    
    actualizada = resultado.rowcount > 0
    
    if conexion_propia:
        conexion.commit()
        conexion.close()
    
    return actualizada