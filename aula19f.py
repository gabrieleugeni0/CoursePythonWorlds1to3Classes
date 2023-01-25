estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: ')).strip()
    estado['Sigla'] = str(input('Sigla: ')).strip().upper()[:2]
    brasil.append(estado.copy())
for est in brasil:
    for key, value in est.items():
        print(f'{key} - {value:<8}', end='    ')
    print()
