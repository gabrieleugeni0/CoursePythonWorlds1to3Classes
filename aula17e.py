valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja digitar mais valores? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('OPCAO INVALIDA! Deseja digitar mais valores? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for posicao, valor in enumerate(valores):
    print(f'Na posicao {posicao} encontrei o valor {valor}!')
print('Cheguei ao final da lista!')