nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input("Edad del empleado"))
salario_empleado = float(input('Salario del empleado'))
es_jefe_departamento = input('Es jefe de departamento?(SI/NO)')

es_jefe_departamento = es_jefe_departamento.lower() == 'si'


print(f'Nombre del empleado: {nombre_empleado}')
print(f'Edad del empleado: {edad_empleado}')
print(f'salario_empleado: {salario_empleado:.2f}')
print(f'Es jefe de departamento: {es_jefe_departamento}')
