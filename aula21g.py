def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


num = list()
fat = list()
for cont in range(0, 3):
    num.append(int(input('Digite um numero: ')))
    fat.append(fatorial(num[cont]))
print(f'Os fatoriais dos numeros {num} sao iguais a {fat}')
