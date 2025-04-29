from random import randint

nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')
year_birth = input('Ingrese el año de nacimineto(YYYY): ')

letras_nombre = nombre.strip().upper()[0:2]
letras_apellido = apellido.strip().upper()[0:2]
letras_year = year_birth.strip().upper()[0:2]

codigo_random = str(randint(1000, 9999))

id = letras_nombre + letras_apellido + letras_year + codigo_random

print(f'Su id correspondiente es el siguiente: {id}')