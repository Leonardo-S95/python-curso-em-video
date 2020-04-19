'''
            DESAFIO 028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import choice
from pygame import mixer
n = 0, 1, 2, 3, 4, 5

print('*' *  12, 'BEM VINDO AO JOGO DA ADIVINHAÇÃO!', '*' * 12, '\n\tEstou pensando em um número entre 0 e 5. Tente acertar!')

n1 = int(input('Digite o número: '))

if choice(n) == n1:
    mixer.init()
    mixer.music.load('YOU WIN!.mp3')
    mixer.music.play()
    input('VOCÊ ACERTOU!!')


else:
    mixer.init()
    mixer.music.load('YOU LOSE!.mp3')
    mixer.music.play()
    input('ERROU FEIO. ERROU FEIO, ERROU RUDE!')


'''
            #RESPOSTA NO VÍDEO
from random import randint
from time import sleep
computador = randint(0, 5)   #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
'''