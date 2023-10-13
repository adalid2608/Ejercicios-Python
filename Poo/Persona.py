'''Declaración de metodos y atributos'''
class Persona():
    nombre = "Adalid"
    apellido = "Islas Quintero"
    sexo = "Masculino"
    edad = 21
    altura = 1.75

    '''Definicion de metodo hablar'''
    def hablar(self, mensaje): 
        return mensaje
    
persona = Persona()

'''Impresion de mensaje, tomando los atributos y llamando al metodo creado'''
print(persona.hablar("Hola, soy {} y mis apellidos son {}, tengo {} , de sexo {} y mido {}"
    .format(Persona.nombre,Persona.apellido, Persona.edad, Persona.sexo, Persona.altura)))