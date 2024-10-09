# función que indique si un número es par o impar

def par_impar(n):
    return 'par' if n % 2 == 0 else 'impar'


for i in range(6):
    print(f'{i} es {par_impar(i)}')

# otra forma


def es_par(n):
    return n % 2 == 0


for i in range(6):
    print(f'{i} es par: {es_par(i)}')
