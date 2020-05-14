'''
            DESAFIO 098
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passos e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
'''

from time import sleep


def contador(a, b, c):

    if c == 0:
        c = 1

    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')

    if a < b:
        for i in range(a, b + 1, c):
            print(f'{i}', end=' ')
            sleep(.3)
        print('FIM!    :D')
    else:
        for i in range(a, b - 1, - c):
            print(f'{i}', end=' ')
            sleep(.3)
        print('FIM!    :D')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print("NOW IT'S YOUR TURN.. Pague apenas um valor simbólico de R$7.690,00 para usar!!")
a = int(input('Início: ').strip())
b = int(input('Fim :').strip())
c = abs(int(input('Passo: ').strip()))

contador(a, b, c)
