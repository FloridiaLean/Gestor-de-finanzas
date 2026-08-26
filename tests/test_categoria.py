from models.categoria import Categoria

def test_crear_categoria():

    categoria = Categoria("Comida")
    
    assert categoria.nombre == "Comida"
    assert categoria.activa is True