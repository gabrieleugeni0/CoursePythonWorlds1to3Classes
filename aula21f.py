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
    return s


soma1 = somar(1, 2, 3)
soma2 = somar(5, 9)
soma3 = somar(9)
soma4 = somar()
print(f'A soma1 vale {soma1}, a soma2 vale {soma2}, a soma3 vale {soma3} e a soma4 vale {soma4}')
print(somar(1, 4, 2))
