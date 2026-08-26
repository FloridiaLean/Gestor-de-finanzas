from models.cuenta import Cuenta
from models.moneda import Moneda
from models.proposito_cuenta import PropositoCuenta

def test_acreditar_monto_positivo():

    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    resultado = cuenta.acreditar(50000)
    
    assert resultado is True
    assert cuenta.saldo == 250000

def test_acreditar_monto_negativo():

    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    resultado = cuenta.acreditar(-50000)
    
    assert resultado is False
    assert cuenta.saldo == 200000

def test_acreditar_monto_cero():

    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    resultado = cuenta.acreditar(0)
    
    assert resultado is False
    assert cuenta.saldo == 200000

def test_debitar_monto_positivo():
    
    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=150000
    )
    
    resultado = cuenta.debitar(10000)
    
    assert resultado is True
    assert cuenta.saldo == 140000
    
def test_debitar_saldo_insuficiente():

    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=50000
    )
    
    resultado = cuenta.debitar(60000)
    
    assert resultado is False
    assert cuenta.saldo == 50000

def test_debitar_monto_cero():

    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    resultado = cuenta.debitar(0)
    
    assert resultado is False
    assert cuenta.saldo == 200000

def test_debitar_monto_negativo():

    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    resultado = cuenta.debitar(-70000)
    
    assert resultado is False
    assert cuenta.saldo == 200000   

def test_debitar_saldo_completo():

    cuenta = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    resultado = cuenta.debitar(200000)
    
    assert resultado is True
    assert cuenta.saldo == 0