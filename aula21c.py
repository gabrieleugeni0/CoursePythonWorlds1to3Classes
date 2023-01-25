def somar(a=0, b=0, c=0):  #parametros opcionais
    """
    -> Faz a soma de tres valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    Funcao criada por Gabriel Rodrigues durante o curso de Python do CursoEmVideo.
    """
    s = a + b + c
    print(f'{a} + {b} + {c} = {s}')


somar(1, 2, 3)
somar(5, 9)
somar(9)
somar()
