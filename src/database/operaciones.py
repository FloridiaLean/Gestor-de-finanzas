from database.database import obtener_conexion
from database.categorias import obtener_categoria
from database.cuentas import obtener_cuenta
from models.operacion import Operacion
from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion

def guardar_operacion(operacion,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    cursor = conexion.execute("""
        INSERT INTO operaciones (
            fecha,
            tipo,
            categoria_id,
            descripcion,
            monto,
            cuenta_origen_id,
            cuenta_destino_id,
            precio_conversion,
            subtipo_conversion
        )
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        operacion.fecha,
        operacion.tipo.value,
        operacion.categoria.id if operacion.categoria else None,
        operacion.descripcion,
        operacion.monto,
        operacion.cuenta_origen.id if operacion.cuenta_origen else None,
        operacion.cuenta_destino.id if operacion.cuenta_destino else None,
        operacion.precio_conversion,
        operacion.subtipo_conversion.value if operacion.subtipo_conversion else None
    ))
    
    conexion.commit()
    
    operacion.id = cursor.lastrowid
    
    if conexion_propia:
        conexion.close()

def obtener_operacion(id_operacion,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
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
    """, (id_operacion,)).fetchone()
    
    if resultado is None:
        if conexion_propia:
            conexion.close()
        return None
    
    categoria = None
    if resultado[3] is not None:
        categoria = obtener_categoria(resultado[3],conexion)
    
    cuenta_origen = None
    if resultado[6] is not None:
        cuenta_origen = obtener_cuenta(resultado[6],conexion)
    
    cuenta_destino = None
    if resultado[7] is not None:
        cuenta_destino = obtener_cuenta(resultado[7],conexion)
    
    tipo = TipoOperacion(resultado[2])
    
    subtipo_conversion = None
    if resultado[9] is not None:
        subtipo_conversion = TipoConversion(resultado[9])
    
    operacion = Operacion(
        id=resultado[0],
        fecha=resultado[1],
        tipo=tipo,
        categoria=categoria,
        descripcion=resultado[4],
        monto=resultado[5],
        cuenta_origen=cuenta_origen,
        cuenta_destino=cuenta_destino,
        precio_conversion=resultado[8],
        subtipo_conversion=subtipo_conversion
    )
    
    if conexion_propia:
        conexion.close()
    
    return operacion

def obtener_operaciones(conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultados = conexion.execute("""
        SELECT id
        FROM operaciones
        ORDER BY id
    """).fetchall()
    
    operaciones = []
    
    for resultado in resultados:
        operacion = obtener_operacion(resultado[0],conexion)
        
        if operacion is not None:
            operaciones.append(operacion)
    
    if conexion_propia:
        conexion.close()
    
    return operaciones

def actualizar_operacion(id_operacion,operacion,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultado = conexion.execute("""
        UPDATE operaciones
        SET
            fecha = ?,
            tipo = ?,
            categoria_id = ?,
            descripcion = ?,
            monto = ?,
            cuenta_origen_id = ?,
            cuenta_destino_id = ?,
            precio_conversion = ?,
            subtipo_conversion = ?
        WHERE id = ?
    """, (
        operacion.fecha,
        operacion.tipo.value,
        operacion.categoria.id if operacion.categoria else None,
        operacion.descripcion,
        operacion.monto,
        operacion.cuenta_origen.id if operacion.cuenta_origen else None,
        operacion.cuenta_destino.id if operacion.cuenta_destino else None,
        operacion.precio_conversion,
        operacion.subtipo_conversion.value if operacion.subtipo_conversion else None,
        id_operacion
    ))
    
    conexion.commit()
    
    actualizado = resultado.rowcount > 0
    
    if conexion_propia:
        conexion.close()
    
    return actualizado