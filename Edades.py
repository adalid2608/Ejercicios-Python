'''Realizar un programa que solicite la edad, el nombre de 10 personas. 
Si el sujeto es mayor de edad agregarlo a un arreglo
y si no es mayor de edad agregarlo a otro arreglo
y al final imprimir los elementos'''
Mayores = []
Menores = []

# Solicitar datos
for j in range(4):    
    nom = input("Ingresa tu nombre \n")
    edad = int(input(f"Ingresa tu edad {nom}\n"))
    if edad>=18:
        Mayores.append(nom)
    else:
        Menores.append(nom)

# Mostrar Arreglos
print("Lista de las personas mayores de edad")
for i in range(len(Mayores)):
    print("- ",Mayores[i])
print("Lista de las personas menores de edad")
for i in range(len(Menores)):
    print("- ",Menores[i])