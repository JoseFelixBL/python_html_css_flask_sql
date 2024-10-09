# encuentre el menor número de una lista

lista = [1, 2, 5, 3, 55, -24, -13]

menor = lista[0]
for el in lista:
    if el < menor:
        menor = el

print(f'EL menor de {lista} es {menor}')

# otra forma
menor = 'init'
for el in lista:
    if menor == 'init':
        menor = el
    elif el < menor:
        menor = el

print(f'EL menor de {lista} es {menor}')
