'''
            DESAFIO 100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''

from random import randint
from time import sleep


def sorteia():
    print(f'Sorteando os 5 números: ')

    for i in range(0, 5):
        numeros.insert(i, randint(0, 9))
        if i != 4:
            print(numeros[i], end=', ')
            sleep(.3)
        else:
            print(f'{numeros[i]}.')
            sleep(.3)


def somaPar():
    s = 0
    for i in numeros:
        if i % 2 == 0:
            s += i
    print(f'A soma dos números pares da lista {numeros} é: {s}.')


numeros = []

sorteia()
somaPar()
