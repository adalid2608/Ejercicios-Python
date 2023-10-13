class Persona():
    nombre = False
    
    '''_init_ es el primero metodo que se ejecuta en toda la clase
    sirve para inicializar los atributos de una clase'''
    def __init__(self):
        print("Has creado el objeto Persona")
    
    '''self es un atributo que reemplaza a nivleglobal
    globaliza ñas variables'''
    def datos(self):
        self.nombre = True
    
persona = Persona()
persona.datos()
print(persona.nombre)