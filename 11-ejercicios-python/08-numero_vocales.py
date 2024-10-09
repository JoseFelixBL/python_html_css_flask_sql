# función que indique cuántas vocales tiene una palabra

def numero_vocales(s):
    total = 0
    for c in s:
        v = c.lower()
        if v in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']:
            total += 1
    return total


print(numero_vocales('Un día vi una vaca vestida de uniforme'))
