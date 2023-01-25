tempo = int(input('Quantos anos de uso tem seu carro? '))
if tempo <= 5:
    print('Seu carro tem {} anos de uso e ainda esta novo!'.format(tempo))
else:
    print('Seu carro tem {} anos de uso e ja esta um pouco velho, talvez esteja na hora de troca-lo!'.format(tempo))
# print('Seu carro tem {} anos de uso e ainda esta novo!'.format(tempo) if tempo <= 5 else 'Seu carro tem {} anos de '
# 'uso e ja esta um pouco velho'
# ', talvez esteja na hora de '
# 'troca-lo!'.format(tempo))
print('--FIM--')
