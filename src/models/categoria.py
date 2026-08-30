from utils.validaciones import validar_nombre

class Categoria:
    
    def __init__(self,nombre,id=None):
        
        validar_nombre(nombre)
        
        self.id = id
        self.nombre = nombre
        self.activa = True
    
    def activar(self):
        self.activa = True
    
    def desactivar(self):
        self.activa = False