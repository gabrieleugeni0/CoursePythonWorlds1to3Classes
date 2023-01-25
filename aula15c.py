nome = 'Gabriel'
idade = 24
salario = 987
print(f'O {nome} tem {idade} anos de idade!') #Python 3.6+
print('O {} tem {} anos de idade!'.format(nome, idade)) #Python 3.5-
print('O %s tem %d anos de idade!' % (nome, idade)) #Python 2
print(f'O {nome:=^15} ganha R${salario:.2f}!')