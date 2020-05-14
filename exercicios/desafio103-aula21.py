'''
            DESAFIO 103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar o ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.
'''


def ficha(nome='<desconhecido>', gols=0):
    print(f'O {nome} fez {gols} gol(s).')


# Programa principal
n = str(input('Nome do jogador: ').strip().title())
g = str(input('Nº de gols: ').strip())

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
