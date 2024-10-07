# Aca va un comentario
if 3 > 5:
    print('Esto no se va a imprimir')

if 5 > 3: # Aca va otro comentario
    print('5 es mayor a 3')

x = 5
y = 'chanchito feliz'

print(x,y)

email = 'chanchito@feliz.com'

print(email)

a, b, c = 'Lala', 'Lele', 'Lili'

print(a, b, c)

valor1 = valor2 = valor3 = 'chanchito feliz'

print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'mundo'

print(inicio + final)

palabra = 'Hola mundo' # string 
oracion = "Hola mundo con comillas dobles" # string

entero = 20 # Integer
conDecimales = 20.2 # float
complejo = 1j

print(palabra, oracion, entero, conDecimales, complejo)

lista = [1, 2, 3]
lista2 = lista.copy()

lista.append(4)

print(lista, lista.count(4), lista2, len(lista), len(lista2))
# lista.clear()

largoLista = len(lista)
largoLista2 = len(lista2)
print(largoLista, largoLista2)

lista = ['Hola', 'Mundo', 'Chanchito feliz']
lista.append(4)
print(lista[2])

print(lista)
lista.pop()
print(lista)
lista.pop()
print(lista)

lista.remove('Hola')
print(lista)

lista = ['Hola', 'Mundo', 'Chanchito feliz']
lista.append(4)
print(lista)

lista.reverse()
print(lista)

lista.remove(4)
lista.append('Chanchito triste')
lista.sort()
print(lista)

tupla = ('hola', 'mundo', 'somos', 'tupla')
print(tupla)

print(tupla.count('hola'), tupla.index('somos'))

listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
print(listaDeTupla)

rango = range(6)
print(rango)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}
print(diccionario)
print(diccionario['nombre'], diccionario['raza'], diccionario.get('edad'))

diccionario['nombre'] = 'Fluffy'
print(diccionario['nombre'], diccionario['raza'], diccionario.get('edad'))

print(len(diccionario))

diccionario['ronronea'] = 'Si'
print(diccionario)

diccionario.pop('ronronea')
print(diccionario)


diccionario['ronronea2'] = 'Si'
print(diccionario)

diccionario.popitem()
print(diccionario)

diccionario['ronronea3'] = 'Si'
print(diccionario)
copiaGatito = diccionario.copy()

del diccionario['ronronea3']
print(diccionario)
print(copiaGatito)

copiaGatito2 = dict(diccionario)
print(diccionario, copiaGatito2)

diccionario.clear()
print(diccionario)
