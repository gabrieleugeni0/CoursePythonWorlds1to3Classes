try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou. Tente novamente!')
except ZeroDivisionError:
    print('Nao existe divisao por zero! Tente novamente!')
except KeyboardInterrupt:
    print('Voce precisa digitar todos os dados! Tente novamente!')
else:
    print(f'{a} / {b} = {r}')
finally:
    print(f'Volte sempre! Muito obrigado!')
