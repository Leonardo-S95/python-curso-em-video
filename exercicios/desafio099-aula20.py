'''
            DESAFIO 099
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep


def maior(* num):
    nmaior = count = 0

    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in num:
        sleep(.4)
        print(f'{i}', end=' ')
        if count == 0:
            nmaior = i
            count += 1
        else:
            if i > nmaior:
                nmaior = i

    print(f'\nForam informados {len(num)} valores no total.')
    print(f'O maior número foi: {nmaior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
