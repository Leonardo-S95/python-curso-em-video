'''
            DESAFIO 030
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
'''

print('*-' * 9, 'DESCUBRA SE SEU NÚMERO É PAR OU ÍMPAR!!!', '*-' * 9)

num = int(input('Digite um número inteiro: '))

if num%2 == 0:
    print('O número que você digitou é par!')

else:
    print('O número que você digitou é ímpar!')


'''
            #RESPOSTA NO VÍDEO

número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))
'''