from models.cuenta import Cuenta
from models.moneda import Moneda
from models.categoria import Categoria
from models.proposito_cuenta import PropositoCuenta
from models.operacion import Operacion
from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion

def test_ingreso():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    categoria_ingreso = Categoria("Ingreso")
    
    ingreso = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.INGRESO,
        categoria=categoria_ingreso,
        descripcion="Cobro quincena",
        monto=50000,
        cuenta_origen=None,
        cuenta_destino=mercado_pago
    )
    
    resultado = ingreso.procesar()
    
    assert resultado is True
    assert mercado_pago.saldo == 250000

def test_ingreso_categoria_inactiva():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    categoria_ingreso = Categoria("Ingreso")
    categoria_ingreso.desactivar()
    
    ingreso = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.INGRESO,
        categoria=categoria_ingreso,
        descripcion="Cobro quincena",
        monto=50000,
        cuenta_origen=None,
        cuenta_destino=mercado_pago
    )
    
    resultado = ingreso.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 200000

def test_ingreso_sin_categoria():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    ingreso = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.INGRESO,
        categoria=None,
        descripcion="Cobro quincena",
        monto=50000,
        cuenta_origen=None,
        cuenta_destino=mercado_pago
    )
    
    resultado = ingreso.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 200000

def test_gasto():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    categoria_comida = Categoria("Comida")
    
    gasto = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.GASTO,
        categoria=categoria_comida,
        descripcion="Hamburguesas",
        monto=20000,
        cuenta_origen=mercado_pago,
        cuenta_destino=None
    )
    
    resultado = gasto.procesar()
    
    assert resultado is True
    assert mercado_pago.saldo == 180000

def test_gasto_saldo_insuficiente():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=10000
    )
    
    categoria_comida = Categoria("Comida")
    
    gasto = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.GASTO,
        categoria=categoria_comida,
        descripcion="Hamburguesas",
        monto=20000,
        cuenta_origen=mercado_pago,
        cuenta_destino=None
    )
    
    resultado = gasto.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 10000

def test_gasto_categoria_inactiva():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    categoria_comida = Categoria("Comida")
    categoria_comida.desactivar()
    
    gasto = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.GASTO,
        categoria=categoria_comida,
        descripcion="Hamburguesas",
        monto=20000,
        cuenta_origen=mercado_pago,
        cuenta_destino=None
    )
    
    resultado = gasto.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 200000

def test_gasto_sin_categoria():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=200000
    )
    
    gasto = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.GASTO,
        categoria=None,
        descripcion="Hamburguesas",
        monto=20000,
        cuenta_origen=mercado_pago,
        cuenta_destino=None
    )
    
    resultado = gasto.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 200000

def test_transferencia():
    
    mercado_pago = Cuenta(
        nombre="Mercado Pago",
        moneda=Moneda.ARS,
        proposito=PropositoCuenta.DISPONIBLE,
        saldo=100000
    )
    efectivo = Cuenta(
            nombre="Billetera",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=10000
    )
    
    categoria_transferencia = Categoria("Transferencia")
    
    transferencia = Operacion(
        fecha="2026/08/13",
        tipo=TipoOperacion.TRANSFERENCIA,
        categoria=categoria_transferencia,
        descripcion="transferencia a efectivo",
        monto=20000,
        cuenta_origen=mercado_pago,
        cuenta_destino=efectivo
    )
    
    resultado = transferencia.procesar()
    
    assert resultado is True
    assert mercado_pago.saldo == 80000
    assert efectivo.saldo == 30000

def test_transferencia_saldo_insuficiente():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=10000
    )
    efectivo = Cuenta(
            nombre="Billetera",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=10000
    )
    
    categoria_transferencia = Categoria("Transferencia")
    
    transferencia = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.TRANSFERENCIA,
            categoria=categoria_transferencia,
            descripcion="transferencia a efectivo",
            monto=20000,
            cuenta_origen=mercado_pago,
            cuenta_destino=efectivo
    )
    
    resultado = transferencia.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 10000
    assert efectivo.saldo == 10000

def test_compra_dolares():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=100000
    )
    ahorro = Cuenta(
            nombre="Exchange",
            moneda=Moneda.USD,
            proposito=PropositoCuenta.AHORRO,
            saldo=500
    )
    
    categoria_conversion = Categoria("Conversion")
    
    conversion = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.CONVERSION,
            categoria=categoria_conversion,
            descripcion="compra de dolares",
            monto=10,
            cuenta_origen=mercado_pago,
            cuenta_destino=ahorro,
            precio_conversion=1500,
            subtipo_conversion=TipoConversion.COMPRA
    )
    
    resultado = conversion.procesar()
    
    assert resultado is True
    assert mercado_pago.saldo == 85000
    assert ahorro.saldo == 510

def test_compra_dolares_saldo_insuficiente():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=100000
    )
    ahorro = Cuenta(
            nombre="Exchange",
            moneda=Moneda.USD,
            proposito=PropositoCuenta.AHORRO,
            saldo=500
    )
    
    categoria_conversion = Categoria("Conversion")
    
    conversion = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.CONVERSION,
            categoria=categoria_conversion,
            descripcion="compra de dolares",
            monto=100,
            cuenta_origen=mercado_pago,
            cuenta_destino=ahorro,
            precio_conversion=1500,
            subtipo_conversion=TipoConversion.COMPRA
    )
    
    resultado = conversion.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 100000
    assert ahorro.saldo == 500

def test_venta_dolares():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=100000
    )
    ahorro = Cuenta(
            nombre="Exchange",
            moneda=Moneda.USD,
            proposito=PropositoCuenta.AHORRO,
            saldo=500
    )
    
    categoria_conversion = Categoria("Conversion")
    
    conversion = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.CONVERSION,
            categoria=categoria_conversion,
            descripcion="venta de dolares",
            monto=100,
            cuenta_origen=ahorro,
            cuenta_destino=mercado_pago,
            precio_conversion=1500,
            subtipo_conversion=TipoConversion.VENTA
    )
    
    resultado = conversion.procesar()
    
    assert resultado is True
    assert mercado_pago.saldo == 250000
    assert ahorro.saldo == 400

def test_venta_dolares_saldo_insuficiente():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=100000
    )
    ahorro = Cuenta(
            nombre="Exchange",
            moneda=Moneda.USD,
            proposito=PropositoCuenta.AHORRO,
            saldo=500
    )
    
    categoria_conversion = Categoria("Conversion")
    
    conversion = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.CONVERSION,
            categoria=categoria_conversion,
            descripcion="venta de dolares",
            monto=1000,
            cuenta_origen=ahorro,
            cuenta_destino=mercado_pago,
            precio_conversion=1500,
            subtipo_conversion=TipoConversion.VENTA
    )
    
    resultado = conversion.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 100000
    assert ahorro.saldo == 500

def test_compra_dolares_monedas_invalidas():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=100000
    )
    ahorro = Cuenta(
            nombre="Exchange",
            moneda=Moneda.USD,
            proposito=PropositoCuenta.AHORRO,
            saldo=50000
    )
    
    categoria_conversion = Categoria("Conversion")
    
    conversion = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.CONVERSION,
            categoria=categoria_conversion,
            descripcion="compra de dolares",
            monto=10,
            cuenta_origen=ahorro,
            cuenta_destino=mercado_pago,
            precio_conversion=1500,
            subtipo_conversion=TipoConversion.COMPRA
    )
    
    resultado = conversion.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 100000
    assert ahorro.saldo == 50000

def test_venta_dolares_monedas_invalidas():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.DISPONIBLE,
            saldo=1000000
    )
    ahorro = Cuenta(
            nombre="Exchange",
            moneda=Moneda.USD,
            proposito=PropositoCuenta.AHORRO,
            saldo=500
    )
    
    categoria_conversion = Categoria("Conversion")
    
    conversion = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.CONVERSION,
            categoria=categoria_conversion,
            descripcion="venta de dolares",
            monto=100,
            cuenta_origen=mercado_pago,
            cuenta_destino=ahorro,
            precio_conversion=1500,
            subtipo_conversion=TipoConversion.VENTA
    )
    
    resultado = conversion.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 1000000
    assert ahorro.saldo == 500

def test_conversion_proposito_invalido():
    
    mercado_pago = Cuenta(
            nombre="Mercado Pago",
            moneda=Moneda.ARS,
            proposito=PropositoCuenta.AHORRO,
            saldo=1000000
    )
    ahorro = Cuenta(
            nombre="Exchange",
            moneda=Moneda.USD,
            proposito=PropositoCuenta.AHORRO,
            saldo=500
    )
    
    categoria_conversion = Categoria("Conversion")
    
    conversion = Operacion(
            fecha="2026/08/13",
            tipo=TipoOperacion.CONVERSION,
            categoria=categoria_conversion,
            descripcion="venta de dolares",
            monto=100,
            cuenta_origen=mercado_pago,
            cuenta_destino=ahorro,
            precio_conversion=1500,
            subtipo_conversion=TipoConversion.VENTA
    )
    
    resultado = conversion.procesar()
    
    assert resultado is False
    assert mercado_pago.saldo == 1000000
    assert ahorro.saldo == 500