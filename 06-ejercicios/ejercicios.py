dato = input('Ingrese dato: ')

# print(dato)

# vamos a tratar de adivinar lo que se encuentra dentro de una lista
lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

if lista.count(dato) > 0:
    print('El dato existe:', dato)
else:
    print('El dato NO existe: ', dato)

