'''Esta funcion hace que el programa no acepte fechas erroneas, 
por ejemplo si se ingresa un mes negativo o 
un mes mayor a 12 que son
los que existen se mostrara un mensaje de error'''
def obtener_signo_zodiacal(dia, mes):
    if mes < 1 or mes > 12:
        return "La fecha que ingreso es incorrecta"
    if mes == 2: 
        if dia < 1 or dia > 29:
            return "La fecha que ingreso es incorrecta"
    elif mes in [4, 6, 9, 11]: 
        if dia < 1 or dia > 30:
            return "La fecha que ingreso es incorrecta"
    else: 
        if dia < 1 or dia > 31:
            return "La fecha que ingreso es incorrecta"

    '''Este es un arreglo que contiene los el mes y el dia en que inicia y 
    el mes y dia en que termina cada signo
    EJEMPLO: Aries inicia el 20 de Marzo y termina el 14 de Abril.
    Asi sucesivamente, el orden es: mes, dia, mes, dia'''
    fechas_zodiacales = [
        (3, 21, 4, 19, "Aries"),
        (4, 20, 5, 20, "Tauro"),
        (5, 21, 6, 20, "Géminis"),
        (6, 21, 7, 22, "Cáncer"),
        (7, 23, 8, 22, "Leo"),
        (8, 23, 9, 22, "Virgo"),
        (9, 23, 10, 22, "Libra"),
        (10, 23, 11, 21, "Escorpio"),
        (11, 22, 12, 21, "Sagitario"),
        (12, 22, 1, 19, "Capricornio"),
        (1, 20, 2, 18, "Acuario"),
        (2, 19, 3, 20, "Piscis"),
    ]

    '''Este ciclo lo que hace es evaluar la fecha introducida y en base a eso retornar el signo'''
    for inicio_mes, inicio_dia, fin_mes, fin_dia, signo in fechas_zodiacales:
        if (mes == inicio_mes and dia >= inicio_dia) or (mes == fin_mes and dia <= fin_dia):
            return f"Tu signo zodiacal es {signo}"
        
    '''Este bloque de codigo lanza una excepcion, esto es en caso de que se introdusca una fecha o algo incorrecto
    si nada falla entonces se ejecuta la parte del else que en teoria es el ciclo for'''
try:
    dia_nacimiento = int(input("Ingresa el día de tu nacimiento: "))
    mes_nacimiento = int(input("Ingresa el mes de tu nacimiento: "))
except ValueError:
    print("Error: Ingresa un número válido para día y mes.")
else:
    resultado = obtener_signo_zodiacal(dia_nacimiento, mes_nacimiento)
    print(resultado)
