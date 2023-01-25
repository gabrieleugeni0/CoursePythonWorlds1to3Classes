print('=' * 40)
print('{} SOMADOR DE VALORES {}'.format((' ' * 9), (' ' * 9)))
print('=' * 40)
qtd = int(input('Quantos valores deseja somar? '))
print('-' * 40)
soma = 0
for contador in range(1, qtd + 1, 1):
    valor = int(input('Digite o {}o valor inteiro: '.format(contador)))
    soma += valor
print('-' * 40)
print('O total foi de: {}'.format(soma))
print('=' * 40)
print('FIM')
