class Categoria:
    
    def __init__(self,nombre):
        
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de la categoria no puede estar vacio")
        
        self.nombre = nombre
        self.activa = True