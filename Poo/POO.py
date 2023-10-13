'''Un objeto es una estructura dedatos personalizada que contiene daros y codigo.

Contiene elementos: Datos o codigo.
¿Que son?: Variables o funciones.
¿Como se llaman?: Atributos o Metodos.
¿Como se identifican?: Mediante sustantivos o mediante verbos.

Objeto: Bicicleta
    Metodos: 
        Girar (Izquierda, Derecha)
        Frenar
        Pedalear
        Avanzar
    Atributos:
        Numero de Rayos
        Diametro de la llanta
        Sillon
        Rueda
        Frenos
        Rayos
        Color'''

class Fabrica():
    pass #Esto determina que es una clase

print(type(Fabrica()))

celular = Fabrica()
print(type(celular))