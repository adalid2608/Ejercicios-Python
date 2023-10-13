class Persona():
    nombre = ""
    apellido = ""
    
    def __init__(self, Nombre, Apellido):
        self.nombre = Nombre
        self.apellido = Apellido
        print("El objeto {} {} ah sido creado".format(self.nombre, self.apellido))
        
    def __str__(self):
        return"El objeto tiene como atributo el nombre {} y el apellido {}".format(self.nombre, self.apellido)

    def __del__(self):
        print("El objeto {} {} ah sido destruido".format(self.nombre, self.apellido))

persona = Persona("Adalid","Islas")
print(str(persona))