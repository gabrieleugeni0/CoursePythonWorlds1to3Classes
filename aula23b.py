while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
    except (ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados que voce digitou. Tente novamente!')
    except ZeroDivisionError:
        print('Nao existe divisao por zero! Tente novamente!')
    else:
        print(f'{a} / {b} = {r}')
        break
    '''finally: nesse caso, com o looping infinito, o finally nao e interessante!'''
print('Volte sempre! Muito obrigado!')
