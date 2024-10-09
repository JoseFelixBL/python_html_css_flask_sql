# while loops

i = 0
while i < 5:
    print(i)
    i += 1

# break y continue

i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

print('Entrando en el segundo while')
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# for loops

usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']
print(usuarios)

# elementos de una lista
for usuario in usuarios:
    print(usuario)

usuario = usuarios[0]
# caracteres de un string
for c in usuario:
    print(c)

# break
for usuario in usuarios:
    if usuario == 'roberto':
        break
    print(usuario)

# continue
for usuario in usuarios:
    if usuario == 'roberto':
        continue
    print(usuario)

# range

print('---')
for x in range(6):
    print(x)

print('---')
for x in range(3, 6):
    print(x)

print('---')
for x in range(3, 30, 5):
    print(x)
else:
    print('Hemos terminado')

# for anidados

usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

edades = [24, 25, 26, 35]

print('---')
for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)
