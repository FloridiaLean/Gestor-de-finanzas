import pytest
from utils.validaciones import (
    validar_nombre,
    validar_fecha
)

def test_validar_nombre():
    
    resultado = validar_nombre("Comida")
    
    assert resultado is None


def test_validar_nombre_vacio():
    
    with pytest.raises(ValueError):
        validar_nombre("")


def test_validar_nombre_espacios():
    
    with pytest.raises(ValueError):
        validar_nombre("   ")

def test_validar_fecha_correcta():
    assert validar_fecha("2026-08-30") is True

def test_validar_fecha_formato_incorrecto():
    assert validar_fecha("30/08/2026") is False

def test_validar_fecha_inexistente():
    assert validar_fecha("2026-02-31") is False