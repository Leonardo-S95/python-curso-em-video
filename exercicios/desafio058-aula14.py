'''
            DESAFIO 058
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando o final quantos palpites foram necessários para vencer.
'''


from random import randint

print('\033[36m=§=\033[m' * 20)
print('\033[32m{:-^60}\033[m'.format(' JOGO DA ADIVINHAÇÃO '))
print('\033[36m=§=\033[m' * 20)

computer = randint(0, 10)
player = int(input('\nEstou pensando em um número entre 0 e 10.\nEm que número estou pensando? '))
cont = 1

while player != computer:
    print('ERRROOOOUU!! Não é o número {}. Tente de novo!'.format(player))
    player = int(input('Adivinhe o número: '))
    cont += 1

print('VOCÊ GANHOU!! Com {} tentativa(s).\n.'.format(cont))



'''
            #RESPOSTA NO VÍDEO
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogado > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
'''