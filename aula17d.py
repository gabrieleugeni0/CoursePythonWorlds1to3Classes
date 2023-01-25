valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...', end=' ')

print('\n')

for valor in range(0, len(valores), 1):
    print(f'Pos: {valor} <-> Val: {valores[valor]}', end='      ')

print('\n')

for posicao, valor in enumerate(valores):
    print(f'Pos: {posicao} <-> Val: {valor}', end='      ')
