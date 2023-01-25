nome = str(input('Qual seu nome? '))
if nome == 'Gabriel':
    print('Que nome bonito voce tem!')
elif nome == 'Joao' or nome == 'Jose' or nome == 'Maria' or nome == 'Ana':
    print('Seu nome e muito popular no Brasil!')
elif nome in 'Vitoria Natalia Lucileia Edina Cecilia':
    print('Que lindo nome feminino!')
else:
    print('Seu nome e bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
