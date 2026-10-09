from models.tipo_operacion import TipoOperacion
from models.tipo_conversion import TipoConversion
from database.operaciones import obtener_operaciones_por_periodo
from database.categorias import obtener_categorias

def obtener_resumen_anual(año,conexion=None):
    
    meses = []
    
    nombres_meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    
    categorias = obtener_categorias(conexion=conexion)
    
    for numero_mes in range(1,13):
        
        gastos_por_categoria = {}
        
        for categoria in categorias:
            gastos_por_categoria[categoria.nombre] = 0
        
        mes = {
            "numero": numero_mes,
            "nombre": nombres_meses[numero_mes - 1],
            "ingresos": 0,
            "gastos": 0,
            "dolares_comprados": 0,
            "dolares_vendidos": 0,
            "gastos_por_categoria": gastos_por_categoria
        }
        
        meses.append(mes)
    
    fecha_desde = f"{año}-01-01"
    fecha_hasta = f"{año}-12-31"
    
    operaciones = obtener_operaciones_por_periodo(fecha_desde,fecha_hasta,conexion=conexion)
    
    for operacion in operaciones:
        mes = int(operacion.fecha[5:7])
        mes_resumen = meses[mes - 1]
        
        if operacion.tipo == TipoOperacion.INGRESO:
            mes_resumen["ingresos"] += operacion.monto
            
        elif operacion.tipo == TipoOperacion.GASTO:
            mes_resumen["gastos"] += operacion.monto
            
            nombre_categoria = operacion.categoria.nombre
            
            if nombre_categoria not in mes_resumen["gastos_por_categoria"]:
                mes_resumen["gastos_por_categoria"][nombre_categoria] = 0
                
            mes_resumen["gastos_por_categoria"][nombre_categoria] += operacion.monto
        
        elif operacion.tipo == TipoOperacion.CONVERSION:
            if operacion.subtipo_conversion == TipoConversion.COMPRA:
                mes_resumen["dolares_comprados"] += operacion.monto
            
            elif operacion.subtipo_conversion == TipoConversion.VENTA:
                mes_resumen["dolares_vendidos"] += operacion.monto
                
    return {
        "año": año,
        "meses": meses
    }