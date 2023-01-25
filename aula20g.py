def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma entre os valores {valores} vale {s}.')

soma(1, 4, 12, 99)