lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# 1o for
print('-' * 30)
for comida in lanche:
    print(comida, end=' ')
# 2o for
print('\n', '-' * 30)
for comida in lanche:
    print(f'Eu vou comer {comida}!')
# 3o for
print('-' * 30)
for cont in range(0, len(lanche), 1):
    print(lanche[cont], end=' ')
# 4o for
print('\n', '-' * 30)
for cont in range(0, len(lanche), 1):
    print(f'Eu vou comer {lanche[cont]}, que esta na posicao {cont}!')
# 5o for
print('-' * 30)
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, que esta na posicao {posicao}!')
