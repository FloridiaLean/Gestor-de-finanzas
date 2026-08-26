import pytest
from utils.validaciones import validar_nombre


def test_validar_nombre():
    
    resultado = validar_nombre("Comida")
    
    assert resultado is None


def test_validar_nombre_vacio():
    
    with pytest.raises(ValueError):
        validar_nombre("")


def test_validar_nombre_espacios():
    
    with pytest.raises(ValueError):
        validar_nombre("   ")