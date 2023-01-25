def dobra(lista):
    for pos in range(0, len(lista)):
        lista[pos] *= 2


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)