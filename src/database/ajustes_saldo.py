from database.database import obtener_conexion
from database.cuentas import (
    obtener_cuenta,
    actualizar_cuenta
)
from models.ajuste_saldo import AjusteSaldo

def guardar_ajuste_saldo(ajuste,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    cursor = conexion.execute("""
        INSERT INTO ajustes_saldo (
            cuenta_id,
            fecha,
            saldo_anterior,
            saldo_nuevo,
            motivo
        )
        VALUES (?,?,?,?,?)
    """, (
        ajuste.cuenta.id,
        ajuste.fecha,
        ajuste.saldo_anterior,
        ajuste.saldo_nuevo,
        ajuste.motivo
    ))
    
    ajuste.id = cursor.lastrowid
    
    if conexion_propia:
        conexion.commit()
        conexion.close()

def obtener_ajuste_saldo(id_ajuste,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
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
    """, (id_ajuste,)).fetchone()
    
    if resultado is None:
        if conexion_propia:
            conexion.close()
        return None
    
    cuenta = obtener_cuenta(resultado[1],conexion)
    
    ajuste = AjusteSaldo(
        id=resultado[0],
        cuenta=cuenta,
        fecha=resultado[2],
        saldo_anterior=resultado[3],
        saldo_nuevo=resultado[4],
        motivo=resultado[5]
    )
    
    if conexion_propia:
        conexion.close()
    
    return ajuste

def ajustar_saldo(cuenta,nuevo_saldo,fecha,motivo,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    saldo_anterior = cuenta.saldo
    
    ajuste = AjusteSaldo(
        cuenta=cuenta,
        fecha=fecha,
        saldo_anterior=saldo_anterior,
        saldo_nuevo=nuevo_saldo,
        motivo=motivo
    )
    
    try:
        cuenta.saldo = nuevo_saldo
        
        actualizar_cuenta(cuenta.id,cuenta,conexion)
        guardar_ajuste_saldo(ajuste,conexion)
        
        if conexion_propia:
            conexion.commit()
    except:
        cuenta.saldo = saldo_anterior
        
        if conexion_propia:
            conexion.rollback()
        
        raise
        
    if conexion_propia:
        conexion.close()
    
    return ajuste