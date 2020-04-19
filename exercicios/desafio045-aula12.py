'''
            DESAFIO 045
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep

print('')
print('{:*^50}'.format(' \033[1;34mJOKENPÔ\033[m '))
print('')

escolha = int(input('\033[1;31mESCOLHA SUA ARMA!\033[m\n'
                    '\033[1m[ 1 ] para PEDRA\n'
                    '[ 2 ] para PAPEL\n'
                    '[ 3 ] para TESOURA\033[m\n'
                    '\033[1;31mDIGITE A OPÇÃO DA ARMA ESCOLHIDA: \033[m'))

print('\nJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.5)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computer = randint(1, 3)

if escolha == computer:
    print('\nVocê escolheu {} e o inimigo escolheu {}.'.format(itens[escolha - 1], itens[computer - 1]))
    print('O combate acabou empatado!')
elif escolha == 1 and computer == 2:
    print('\nVocê escolheu {} e o inimigo escolheu {}.'.format(itens[escolha - 1], itens[computer - 1]))
    print('Sua pedra foi brutalmente embrulhada pelo papel!\n\033[1;31mYOU LOSE!\033[m')
elif escolha == 1 and computer == 3:
    print('\nVocê escolheu {} e o inimigo escolheu {}.'.format(itens[escolha - 1], itens[computer - 1]))
    print('Sua pedra massacrou a tesoura!\n\033[1;32mYOU WIN!\033[m ')
elif escolha == 2 and computer == 1:
    print('\nVocê escolheu {} e o inimigo escolheu {}.'.format(itens[escolha - 1], itens[computer - 1]))
    print('Seu papel sufocou hardmente a pobre coitada da pedra inimiga!\n\033[1;32mYOU WIN\033[m')
elif escolha == 2 and computer == 3:
    print('\nVocê escolheu {} e o inimigo escolheu {}.'.format(itens[escolha - 1], itens[computer - 1]))
    print('Seu papel foi estraçalhado pela tesoura!\n\033[1;31mYOU LOSE!\033[m')
elif escolha == 3 and computer == 1:
    print('\nVocê escolheu {} e o inimigo escolheu {}.'.format(itens[escolha - 1], itens[computer - 1]))
    print('Sua tesoura foi destroçada pela pedra!\n\033[1;31mYOU LOSE!\033[m')
elif escolha == 3 and computer == 2:
    print('\nVocê escolheu {} e o inimigo escolheu {}.'.format(itens[escolha - 1], itens[computer - 1]))
    print('Sua tesoura fez picadinho do papel inimigo!\n\033[1;32mYOU WIN!\033[m')
if escolha < 1 or escolha > 3:
    print('\nESCOLHA UMA DAS OPÇÕES ACIMA, GAROTO!')
