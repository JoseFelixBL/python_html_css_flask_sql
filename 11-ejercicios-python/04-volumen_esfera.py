# Volumen de una esfera por su radio
# volumen = 4/3 * pi * r**3

def calcula_volumen(r):
    return 4 / 3 * 3.14 * r**3


r = 6
resultado = calcula_volumen(r)
print(f'Volumen de esfera de radio {r} es {resultado}')
