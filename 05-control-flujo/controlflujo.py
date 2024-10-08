
if 2 < 5:
    print('2 es menor que 5')

# a == b
# a < b
# a != b
# a <= b
# a >= b


if 2 == 2:
    print('2 es igual a 2')

if 2 == 3:
    print('2 es igual a 3')

if 2 > 5:
    print('2 es mayor que 5')

if 5 > 2:
    print('5 es mayor que 2')

if 2 != 2:
    print('2 es distinto que 2')

if 3 != 2:
    print('3 es distinto que 2')

if 3 >= 2:
    print('3 es mayor o igual que 2')

if 3 <= 3:
    print('3 es menor o igual que 3')

# Ahora agregamos "elif" y "else"
if 2 > 5:
    print('lala')
elif 2 < 5:
    print('2 es menor a 5 en elif')
elif 2 < 5:
    print('2 es menor a 5 en segundo elif')
else:
    print('SOlo si todo lo anterior es falso')

# if cortos y ternarios
if 2 < 5: print('if de una linea')

# Operador TERNARIO
print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false')

# and y or

if 2 < 5 and 3 > 2:
    print('Ambas devuelven true')

if 2 < 5 and 3 < 2:
    print('Hay una falsa, esto no se  mostrara')

if 1 < 0 or 1 > 0:
    print('Una de las 2 condiciones devolvio true')

if 1 < 0 or 1 < 0:
    print('Si ambas condiciones son false esto no se ejecuta')


