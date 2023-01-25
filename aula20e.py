def contador(*num):
    tamanho = len(num)
    soma = 0
    for c in num:
        soma += c
    print(f'Recebi os valores {num}, sendo ao todo {tamanho} numeros que somados valem {soma}!')


contador(1, 2, 3)
contador(0, 0, 0, 0, 0, 0, 0)
contador(10, 9, 8, 7)
contador(32, 12, 56, 2342, 56, 0, 99999)
