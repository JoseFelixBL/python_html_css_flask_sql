
# Clases - como el plano de una casa

class UsuarioInicial:
    # Propiedades del UsuarioInicial
    nombre = "Felipe"
    apellido = "Feliz"

# Instanciar una clase
usuario = UsuarioInicial()

# El objeto instanciado, o sea, la casa hecha a partir del plano
print(usuario)

# Las propiedades del objeto
print(usuario.nombre, usuario.apellido)
print('---')

# init() se ejecuta al crear una instancia de cada objeto

class Usuario:
    def __init__(self, nombre, apellido):
        # valores iniciales de las propiedades: parametros de creacion
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)

usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Chanchito', 'Feliz')

print(usuario.nombre, usuario.apellido)
print(usuario2.nombre, usuario2.apellido)

usuario.saludo()
usuario2.saludo()

#Podemos cambiar el valor de las propiedades de un objeto

print('---')
usuario.saludo()
usuario.nombre = 'Cahnchito'
usuario.saludo()
print('---')

# ...y tambien podemos eliminar una propiedad

del usuario.nombre
try:
    usuario.saludo()
except:
    print('No se puede ejecutar el metodo saludo porque no existe la propiedad nombre')
print('---')

# podemos eliminar un objeto que hayamos creado

print('Usuario2: ', usuario2)
del usuario2
try:
    print('Usuario2: ', usuario2)
except:
    print('El usuario2 no esta definido')

print('---')

# Herencia

class Admin(Usuario):
    def superSaludo(self):
        print('Hola, me llamo', self.nombre, 'y soy administrador')

admin = Admin('Super', 'Feliz')

admin.saludo()
admin.superSaludo()

