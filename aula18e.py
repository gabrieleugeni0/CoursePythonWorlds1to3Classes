galera = list()
dadostemporarios = list()
while True:
    dadostemporarios.append(str(input('Nome: ')))
    dadostemporarios.append(int(input('Idade: ')))
    galera.append(dadostemporarios[:])
    dadostemporarios.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('OPCAO INVALIDA! Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(galera)