from datetime import datetime


print(f'---Digita 1 para recibir el nombre y año de nacimiento---')
print(f'---Digita 2 para calcular la edad y mostrar en la pantalla---')
print(f'---Digita 3 para mostrar saludo de buenas noches al usuario---')
print(f'---Digita 4 para contarle cuantos años tendra en el 2030---')
print(f'---Digita 5 para Salir---')

opcion = 100
UserDate=0

while opcion != 5:

    opcion= int(input('Digite la opcion del Menu: '))
    
    if(opcion==2):
        UserDate=int(input("Digita el año de nacimiento: "))
        edad = (2022-UserDate)
        print("La edad es: ",edad)