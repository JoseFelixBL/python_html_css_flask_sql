# Hacer una calculadora que solo sume

primero = input('Ingrese el primer numero: ')
segundo = input('Ingrese el segundo numero: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('Ingresaste mal un dato, prueba de nuevo solo con numeros')
else:
    print(primero + segundo)
