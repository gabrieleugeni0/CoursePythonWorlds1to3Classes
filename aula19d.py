pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')
for k, v in pessoas.items():
    print(f'{k}: {v}')
del pessoas['sexo']
print(pessoas)
pessoas['nome'] = 'Marcos'
print(pessoas)