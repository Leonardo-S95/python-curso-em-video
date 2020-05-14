'''
            DESAFIO 101
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''


def voto(ano):

    from datetime import datetime

    idade = datetime.now().year - ano

    if idade >= 18 and idade <= 70:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO.'
    elif idade >= 16 and idade < 18 or idade > 70:
        return f'Com {idade} anos, o voto é OPCIONAL.'
    else:
        return f'Com {idade} anos, o voto é NEGADO.'


# Programa principal
print(voto(1995))
