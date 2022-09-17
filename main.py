print(f'---Digita 1 para recibir el nombre y año de nacimiento---')
print(f'---Digita 2 para calcular la edad y mostrar en la pantalla---')
print(f'---Digita 3 para mostrar saludo de buenas noches al usuario---')
print(f'---Digita 4 para contarle cuantos años tendra en el 2030---')
print(f'---Digita 5 para Salir---')

opcion = 100

while opcion != 5:
    opcion = int(input("Digita una opción:  "))
    if(opcion == 1):
        nombre = input("Digita tu nombre:  ")
        fechaNacimiento = int(input("Digita año de nacimiento:  "))
