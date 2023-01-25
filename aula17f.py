a = [2, 3, 4, 7]
b = a
c = a[:]
b[2] = 55
c[2] = 'x'
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
