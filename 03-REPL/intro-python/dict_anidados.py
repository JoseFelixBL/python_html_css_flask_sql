# Diccionarios anidados y constructor dict

gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12
    }
}

print(gatitos)

gatitos.clear()
print(gatitos)

# Usando variables
fluffy = {
        "nombre": "Fluffy",
        "edad": 4
}
    
mamba = {
        "nombre": "Black Mamba",
        "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

# Usando el constructor dict()
perritos = dict(nombre="Chanchito feliz", edad=6)
print(perritos)

#
# Booleanos
#
verdadero = True
falso = False

print(verdadero, falso)
