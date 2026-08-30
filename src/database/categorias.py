from database.database import obtener_conexion
from models.categoria import Categoria

def guardar_categoria(categoria,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    cursor = conexion.execute("""
        INSERT INTO categorias (
            nombre,
            activa
        )
        VALUES (?,?)
    """, (
        categoria.nombre,
        categoria.activa
    ))
    
    conexion.commit()
    
    categoria.id = cursor.lastrowid
    
    if conexion_propia:
        conexion.close()

def obtener_categoria(id_categoria,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultado = conexion.execute("""
        SELECT id,nombre,activa
        FROM categorias
        WHERE id = ?
    """, (id_categoria,)).fetchone()
    
    if conexion_propia:
        conexion.close()
    
    if resultado is None:
        return None
    
    categoria = Categoria(
        id=resultado[0],
        nombre=resultado[1]
    )
    
    categoria.activa=bool(resultado[2])
    
    return categoria

def actualizar_categoria(id_categoria,categoria,conexion=None):
    
    conexion_propia = False
    
    if conexion is None:
        conexion = obtener_conexion()
        conexion_propia = True
    
    resultado = conexion.execute("""
        UPDATE categorias
        SET nombre = ?,
            activa = ?
        WHERE id = ?
    """, (
        categoria.nombre,
        categoria.activa,
        id_categoria
    ))
    
    conexion.commit()
    
    actualizada = resultado.rowcount > 0
    
    if conexion_propia:
        conexion.close()
    
    return actualizada