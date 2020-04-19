'''
            DESAFIO 063
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência
de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
'''

print('\033[30;41m~=#=~\033[m' * 10)
print('\033[36m{:^50}\033[m'.format('SEQUÊNCIA DE FIBONACCI'))
print('\033[30;41m~=#=~\033[m' * 10)
print('')

n = int(input('Digite quantos números da SEQUÊNCIA DE FIBONACCI deseja ver: '))
t1 = 0
t2 = 1
count = 3

print('{} → {}'.format(t1, t2), end='')

while count <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('')
