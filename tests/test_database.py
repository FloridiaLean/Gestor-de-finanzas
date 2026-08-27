from database.database import obtener_conexion

def test_obtener_conexion():
    
    conexion = obtener_conexion(":memory:")
    
    assert conexion is not None
    
    conexion.close()