
# Ejercicio herencia
# Crear clases de gato y perro ...

class GatoIni:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un gato y mi sonido es el', self.onomatopeya)

class PerroIni:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un perro y mi sonido es el', self.onomatopeya)

gatoIni = GatoIni('FluffyIni', 'maullido')
gatoIni.saludo()

perroIni = PerroIni('FirulaisIni', 'ladrido')
perroIni.saludo()

print('---')

# Crearemos una clase Animal y de ella heredan Gato y Perro y Canario

class Animal():
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un', self.tipo, ', me llamo', self.nombre, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido!')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro!!!')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()

