# Hacer una calculadora que solo sume

primero = input('Ingrese el primer numero: ')
try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('Ingresaste mal el primer dato: prueba de nuevo solo con numeros')
    exit()

segundo = input('Ingrese el segundo numero: ')
try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('Ingresaste mal el segundo dato: prueba de nuevo solo con numeros')
    exit()

print(primero + segundo)
