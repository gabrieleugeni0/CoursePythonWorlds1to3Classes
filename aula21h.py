def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print(f'O numero {num} e PAR!')
else:
    print(f'O numero {num} e IMPAR!')