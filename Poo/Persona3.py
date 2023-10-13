class Persona():
    nombre = ""
    apellido = ""
    
    def __init__(self, Nombre, Apellido):
        self.nombre = Nombre
        self.apellido = Apellido
        print("Has creado el objeto Persona llamado {} {}"
            .format(Nombre, Apellido))
persona = Persona("Adalid", "Islas")