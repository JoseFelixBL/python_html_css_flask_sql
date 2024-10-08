# Hacer una calculadora con las 4 operaciones

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

simbolo = input('Ingrese operacion: (+, -, *, /) ')
if simbolo == '+':
    print(primero + segundo)
elif simbolo == '-':
    print(primero - segundo)
elif simbolo == '*':
    print(primero * segundo)
elif simbolo == '/':
    print(primero / segundo)
else:
    print('Simbolo incorrecto, prueba con una de las cuatro operaciones: +, -, *, /')
