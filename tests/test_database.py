from database.database import obtener_conexion
from database.schema import(
    crear_tabla_cuentas,
    crear_tabla_categorias,
    crear_tabla_operaciones,
    crear_tabla_ajustes_saldo
)

def test_obtener_conexion():
    
    conexion = obtener_conexion(":memory:")
    
    assert conexion is not None
    
    conexion.close()

def test_crear_tabla_ajustes_saldo():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_ajustes_saldo(conexion)
    
    resultado = conexion.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        AND name = 'ajustes_saldo'
    """).fetchone()
    
    assert resultado is not None
    assert resultado[0] == "ajustes_saldo"
    
    conexion.close()

def test_estructura_tabla_ajustes_saldo():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_cuentas(conexion)
    crear_tabla_ajustes_saldo(conexion)
    
    columnas = conexion.execute("""
        PRAGMA table_info(ajustes_saldo)
    """).fetchall()
    
    nombres = [columna[1] for columna in columnas]
    
    assert "id" in nombres
    assert "cuenta_id" in nombres
    assert "fecha" in nombres
    assert "saldo_anterior" in nombres
    assert "saldo_nuevo" in nombres
    assert "motivo" in nombres
    
    conexion.close()