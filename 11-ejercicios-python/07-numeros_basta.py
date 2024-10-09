# app que reciba nñumneros hasta decir "basta" y luego los sume

lista = []

print('Ingrese números hasta decir "basta"')
while True:
    n = input()
    if n == 'basta':
        break
    try:
        ent = int(n)
        lista.append(ent)
    except:
        print('Dato inválido')
        exit()

suma = 0
for n in lista:
    suma += n

print(f'La suma de {lista} es {suma}')
