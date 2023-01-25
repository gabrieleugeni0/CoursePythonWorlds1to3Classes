def contador(i, f, p):
    """
    -> Faz uma contagem do inicio ao fim com um passo determinado e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Funcao criada por Gabriel Rodrigues durante o curso de Python do CursoEmVideo
    """
    if p == 0:
        p = 1
    if p < 0:
        p = -p
    if f > i:
        for cont in range(i, (f + 1), p):
            print(cont, end=' ')
        print('FIM')
    elif i > f:
        for cont in range(i, (f - 1), -p):
            print(cont, end=' ')
        print('FIM')


contador(0, 10, 0)
print('-' * 60)
help(contador)
