'''
            DESAFIO 088
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

sorteio = []
completa = []

num = randint(1, 60)
count = 0

print('=-' * 30)
print('GERADOR DE PALPITE MEGA SENA'.center(60))
print('=-' * 30)
print()

quant = int(input('Quantos jogos deseja gerar? '))

while True:
    count += 1

    for i in range(0, 6):

        if i == 0:
            sorteio.append(num)
        else:
            while num in sorteio:
                num = randint(1, 60)
            sorteio.append(num)

    completa.append(sorteio[:])
    sorteio.clear()

    if count == quant:
        break

for i in range(0, quant):
    completa[i].sort()

print(f'\n#-#-#-#-# Sorteando {quant} JOGOS  #-#-#-#-#\n')
for i in range(0, quant):
    sleep(.5)
    print(f'Jogo {i + 1}: {completa[i]}')

print('\n--------------- FIM ---------------')
