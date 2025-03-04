#Conversion de tipos de datos

#Convertir de cadena a numero

numero_cadena = '10'

numero_entero = int(numero_cadena)

print(type(numero_cadena))

print(type(numero_entero))


#Convertir cadena a flotante

numero_cadena = '3.14'
numero_flotante = float(numero_cadena)

print(type(numero_cadena))
print(type(numero_flotante))

#Convertir de numero a cadena

numero_entero = 25
numero_cadena = str(numero_entero)

print(type(numero_entero))
print(type(numero_cadena))

#Convertir a booleano
#Si el valor es 0, cadena vacia, o None, entonces regresa false
#Regresa True, si el valor es distinto de 0, si es distintio de cadena vacia
#Y tambien si es distinto de None

numero_entero = ' '
booleano = bool(numero_entero)
print(booleano)