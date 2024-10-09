import os

# Para comprobar que el fichero existe
if os.path.exists('chanchito.txt'):
    # Para eliminar el fichero
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

# Para eliminar un directorio
os.rmdir('micarpeta')
