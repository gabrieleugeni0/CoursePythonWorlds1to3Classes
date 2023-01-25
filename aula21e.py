def funcao():
    global n1
    n1 = 4
    print(f'n1 dentro (local) vale {n1}')


n1 = 0
funcao()
print(f'n1 fora (global) vale {n1}')
