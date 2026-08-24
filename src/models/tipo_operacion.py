from enum import Enum

class TipoOperacion(Enum):
    
    INGRESO = "Ingreso"
    GASTO = "Gasto"
    TRANSFERENCIA = "Transferencia"
    COMPRA_DOLARES = "Compra de dólares"
    VENTA_DOLARES = "Venta de dólares"