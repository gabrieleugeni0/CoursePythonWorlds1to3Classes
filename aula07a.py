n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
mod = n1 % n2
print('{} mais {} vale {}'.format(n1, n2, s), end=' ')
print('{} vezes {} vale {}'.format(n1, n2, m))
print('{} dividido \npor {} vale {:.3f}'.format(n1, n2, d))
print('A divisao inteira entre {} e {} vale {}'.format(n1, n2, di))
print('O modulo da divisao entre {} e {} vale {}'.format(n1, n2, mod))

