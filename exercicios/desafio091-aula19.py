'''
            DESAFIO 091
Crie um programa onde 4 jogadores jogue um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em
ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

print('-' * 50)
print('JOGO QUE VOCÊ NÃO JOGA (PERDI, BTW)'.center(50))
print('-' * 50)
print()

dado = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)
        }

ranking = []
count = 1

for i, j in dado.items():
    print(f'O {i} jogou o dado e tirou {j}.')
    sleep(.7)

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

print()
print('=' * 20, 'RESULTADO', '=' * 20)
print()

for i in ranking:
    print(f'{count}º LUGAR: {i[0]} com {i[1]} no dado.')
    count += 1
    sleep(.7)
