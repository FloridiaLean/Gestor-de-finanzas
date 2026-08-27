import sqlite3

RUTA_BASE_DATOS = "data/finanzas.db"

def obtener_conexion(ruta=RUTA_BASE_DATOS):
    
    return sqlite3.connect(ruta)