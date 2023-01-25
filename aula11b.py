a = 3
b = 5
print('Os valores sao \033[1;33m{}\033[m e \033[4;35m{}\033[m!!!'.format(a, b))

print('Os valores sao {}{}{} e {}{}{}!!!'.format('\033[1;33m', a, '\033[m', '\033[4;35m', b, '\033[m'))
