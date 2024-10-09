# función que reciba nombre y apellido y los agregue a un archivo

def nombre_a_archivo(nombre, apellido):
    f = open('nombre_y_apellido.txt', 'a')
    f.write(nombre + ' ' + apellido + '\n')
    f.close()


nombre_a_archivo('Chanchito', 'Feliz')
nombre_a_archivo('Felipe', 'Hermoso')
