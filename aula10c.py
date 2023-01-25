n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('Sua media foi {} e voce esta APROVADO!'.format(m))
else:
    if m >= 4:
        print('Sua media foi {} e voce esta de RECUPERACAO!'.format(m))
    else:
        print('Sua media foi {} e voce infelizmente foi REPROVADO'.format(m))
