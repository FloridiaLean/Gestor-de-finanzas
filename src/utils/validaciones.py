def validar_nombre(nombre):
    
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacio")