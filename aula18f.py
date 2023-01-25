galera = list()
dadostemporarios = list()
totmaior = totmenor = 0
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

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} atingiu a maioridade, pois tem {pessoa[1]} anos de idade!')
        totmaior += 1
    else:
        print(f'{pessoa[0]} e MENOR, pois tem {pessoa[1]} anos de idade!')
        totmenor += 1

print(f'No total temos {totmaior} maiores e {totmenor} menores de idade.')