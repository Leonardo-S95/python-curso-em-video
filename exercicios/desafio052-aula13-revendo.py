'''
            DESAFIO 052
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


n = int(input('Digite um número: '))
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')

print('\n\033[mO número {} foi dividido {} vezes.'.format(n, total))

if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
'''

'''
            DESAFIO 052 (REFAZENDO)
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

n = int(input('Escreva um numerito para saberes se és primito: '))
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{} \033[m'.format(i), end='')

print('\nO numerito {} foi divididito {} vezita(s).'.format(n, total))

if total == 2:
    print('\033[30mO numerito és primito!\033[m')
else:
    print('\033[30mSu numerito no és primito!   :(')
