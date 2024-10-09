c = open('chanchito.txt')
print(c.read())
c.close()

# Para hacer un readline directo...
c = open('chanchito.txt')
for x in c:
    print(x)

c.close()

# Para abrir en modo escritura con append
c = open('chanchito.txt', 'a')
c.write('\nAgregaremos una nueva linea a nuestro archivo')
c.close()

# Com 'w' reemplazamos todo el contenido de nuestro 
# archivo por lo que le escribamos ahora

