from enum import Enum

class TipoOperacion(Enum):
    
    INGRESO = "Ingreso"
    GASTO = "Gasto"
    TRANSFERENCIA = "Transferencia"
    CONVERSION = "Conversion"