galera = [['Joao', 25], ['Maria', 39], ['Antonio', 18]]
for pessoa in galera:
    print(pessoa)
print('-' * 40)
for pessoa in galera:
    print(f'Nome: {pessoa[0]}', end=' - ')
    print(f'Idade: {pessoa[1]}')
print('-' * 40)
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade!')

