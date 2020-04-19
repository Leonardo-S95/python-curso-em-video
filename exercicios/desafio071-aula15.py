'''
            DESAFIO 071
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

from math import floor

print('=' * 40)
print('BANCO LBS'.center(40))
print('=' * 40)

nota50 = nota20 = nota10 = nota1 = 0

valor = int(input('Que valor você deseja sacar? R$'))

if valor >= 50:
    nota50 = valor / 50
    valor = valor % 50

if valor >= 20:
    nota20 = valor / 20
    valor = valor % 20

if valor >= 10:
    nota10 = valor / 10
    valor = valor % 10

if valor < 10:
    nota1 = valor

print(f'{floor(nota50)} nota(s) de R$50\n{floor(nota20)} nota(s) de R$20\n'
      f'{floor(nota10)} nota(s) de R$10\n{nota1} nota(s) de R$1')
