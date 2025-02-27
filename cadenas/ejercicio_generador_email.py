nombre = 'Isaac Uribe Arciniegas'
empresa = 'Pragma'
dominio = '.com.co'

nombre = nombre.lower()
nombre = nombre.replace(' ', '.')

empresa = empresa.lower()
empresa.replace(' ', '')

resultado = nombre + '@' + empresa + dominio

print(nombre)
print(empresa)
print(resultado)



#metodo .strip() quita los espacios al inicio y al final