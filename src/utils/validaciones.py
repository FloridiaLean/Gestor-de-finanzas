from datetime import datetime

def validar_nombre(nombre):
    
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacio")

def validar_fecha(fecha):
    
    try:
        datetime.strptime(fecha,"%Y-%m-%d")
        return True
    except ValueError:
        return False