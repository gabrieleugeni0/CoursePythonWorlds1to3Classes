c = ''
par = 0
impar = 0
while c != 'N':
    valor = int(input('Digite um valor: '))
    if (valor % 2) == 0:
        par += 1
    else:
        impar += 1
    c = str(input('Deseja digitar mais um valor? [S/N] ')).upper()
print('Foram digitados {} valores PARES e {} valores impares!'.format(par, impar))
print('FIM')
