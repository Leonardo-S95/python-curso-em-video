'''
            DESAFIO 074
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)

numeros = (a, b, c, d, e)

print(f'Os números sorteador foram: {numeros}'.replace('(', '').replace(')', ''))

ordem = sorted(numeros)

print(f'O maior valor foi: {ordem[4]}.\nO menor valor foi: {ordem[0]}.')
