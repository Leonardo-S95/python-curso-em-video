'''
            DESAFIO 102
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(n=0, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    count = n

    for i in range(1, n + 1):
        f *= n
        n -= 1
        if show == True and i != count:
            print(f'{n + 1}', end=' x ')
        elif show == True and i == count:
            print(f'{n + 1}', end=' = ')
    return f


print(fatorial(5, show=True), '\n')
help(fatorial)



'''
            # RESOLUÇÃO CURSO EM VÍDEO


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
        print(c, end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        f *= c
    return f
    

# Programa principal
print(fatorial(5, show=True))
help(fatorial)
'''