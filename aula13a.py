inicio = int(input('Inicio da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo da contagem: '))
for contador in range(inicio, fim + 1, passo):
    print(contador)
print('FIM')
