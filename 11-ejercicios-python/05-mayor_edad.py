# función que diga si un usuario es mayor de edad

def es_mayor(persona):
    return persona.edad > 17


class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


usuario = Usuario('Chanchito', 17)
usuario2 = Usuario('Felipe', 25)

for chico in [usuario, usuario2]:
    print(f'{chico.nombre} es mayor de edad: {es_mayor(chico)}')
