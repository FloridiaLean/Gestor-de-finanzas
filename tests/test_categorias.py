from database.database import obtener_conexion
from database.categorias import (
    guardar_categoria,
    obtener_categoria,
    actualizar_categoria
)
from database.schema import crear_tabla_categorias
from models.categoria import Categoria

def test_guardar_categoria():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_categorias(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_categoria(categoria,conexion)
    
    resultado = conexion.execute("""
        SELECT nombre, activa
        FROM categorias
        WHERE nombre = ?
    """, ("Comida",)).fetchone()
    
    assert resultado is not None
    assert resultado[0] == "Comida"
    assert resultado[1] == 1
    
    conexion.close()

def test_obtener_categoria():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_categorias(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    ) 
    
    guardar_categoria(categoria,conexion)
    
    categoria_obtenida = obtener_categoria(1,conexion)
    
    assert categoria_obtenida is not None
    assert categoria_obtenida.nombre == "Comida"
    assert categoria_obtenida.activa is True
    
    conexion.close()

def test_obtener_categoria_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_categorias(conexion)
    
    categoria_obtenida = obtener_categoria(999,conexion)
    
    assert categoria_obtenida is None
    
    conexion.close()

def test_actualizar_categoria():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_categorias(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    guardar_categoria(categoria,conexion)
    
    categoria_actualizada = Categoria(
        nombre="Restaurantes"
    )
    
    categoria_actualizada.desactivar()
    
    resultado = actualizar_categoria(1,categoria_actualizada,conexion)
    
    assert resultado is True
    
    categoria_obtenida = obtener_categoria(1,conexion)
    
    assert categoria_obtenida.nombre == "Restaurantes"
    assert categoria_obtenida.activa is False
    
    conexion.close()

def test_actualizar_categoria_inexistente():
    
    conexion = obtener_conexion(":memory:")
    
    crear_tabla_categorias(conexion)
    
    categoria = Categoria(
        nombre="Comida"
    )
    
    resultado = actualizar_categoria(999,categoria,conexion)
    
    assert resultado is False
    
    conexion.close()