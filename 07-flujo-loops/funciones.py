# Funciones

def miFuncion():
    print("Mi primera funcion")

for _ in range(6):
    miFuncion()
print('---')

# Pasar argumentos

def imprimeDato(argumentoUno):
    print('Mi argumento es', argumentoUno)

imprimeDato('parametro 1')
print('---')

def imprimeDosDatos(nombre, apellido):
    print('El nombre completo es:', nombre, apellido)

imprimeDosDatos('Chanchito', 'Feliz')
print('---')

# cantidad variable de argumentos
# Se le pasa UNA TUPLA, recibe un *<variable>, imprime una TUPLA

def imprimeVariosDatos(*nombre):
    print('El nombre completo es:', nombre)
    print('El tercer nombre de la tupla es:', nombre[2])

imprimeVariosDatos('Chanchito', 'Feliz', 'Lala', 'Lele')
print('---')

# Nombrar los argumentos por sus nombres

def nombreCompleto(apellido, nombre):
    print('El nombre completo es:', nombre, apellido)

nombreCompleto(nombre='Chanchito', apellido='Feliz')
print('---')

# Agrupar los argumentos como un diccionario: **kwargs
# Se llaman con parametros por nombre como en el caso anterior

def nombreCompletoDict(**kwargs):
    print('El nombre completo es:', kwargs['nombre'], kwargs['apellido'])

nombreCompletoDict(nombre='Chanchito', apellido='Feliz')
print('---')

# Argumento con valor por defecto

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

miFuncion2('Batman')
miFuncion2()
print('---')

# Pasar una lista como argumento

def miFuncionLista(lista):
    for el in lista:
        print(el)

miFuncionLista(['Chanchito', 'Feliz'])
print('---')

# Retornar un valor

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i 

nombres = concatenaNombres(['Chanchito', 'Feliz'])
print(nombres)
print('---')


