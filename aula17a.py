lista = ['a', 'e', 'i', 'o', 'u']
print(lista)

lista.append('x')
print(lista)

lista.insert(0, 'y')
print(lista)

del lista[0]
print(lista)

lista.pop(1)
print(lista)

lista.pop()
print(lista)

lista.remove('i')
print(lista)

if 'z' in lista:
    lista.remove(z)
print(lista)