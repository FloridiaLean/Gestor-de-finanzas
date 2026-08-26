from models.categoria import Categoria

def test_crear_categoria():

    categoria = Categoria("Comida")
    
    assert categoria.nombre == "Comida"
    assert categoria.activa is True

def test_categoria_se_crea_activa():
    
    categoria = Categoria("Comida")
    
    assert categoria.activa is True

def test_desactivar_categoria():
    
    categoria = Categoria("Comida")
    
    categoria.desactivar()
    
    assert categoria.activa is False

def test_activar_categoria():
    
    categoria = Categoria("Comida")
    
    categoria.desactivar()
    categoria.activar()
    
    assert categoria.activa is True