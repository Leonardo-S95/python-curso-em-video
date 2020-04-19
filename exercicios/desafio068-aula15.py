'''
            DESAFIO 068
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

print('#-' * 15)
print('   JOGUINHO DO PAR OU ÍMPAR')
print('#-' * 15)

player = maquina = perder = contador = 0

while perder == 0:
    player = int(input('Digite um número: '))
    escolha = input('Par ou ímpar? [P/I]').upper()[0].strip()
    maquina = randint(0, 10)

    while escolha not in 'PI':
        escolha = input('Opção inválida! Par ou Ímpar? [P/I]').upper()[0].strip()

    if (player + maquina) % 2 == 0 and escolha == 'P' or (player + maquina) % 2 == 1 and escolha == 'I':
        print(f'\nVocê escolheu {player} e o computador {maquina}. Total = {player + maquina} = {escolha}!'
              f'\nYOU WIN!!\n')
        contador += 1
    else:
        print('\nGAME OVER!')
        break

print(f'Você venceu {contador} vez(es).')
