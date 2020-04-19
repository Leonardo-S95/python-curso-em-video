'''                DESAFIO 016
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''



from math import trunc
num = float(input('Digite um número qualquer: '))
print('A porção inteira do número {} é \033[4m{}\033[m.'.format(num, trunc(num)))



'''
                OU
num = float(input('Digite um número qualquer: '))
print('A porção inteira do número {} é {}.'.format(num, int(num)))
'''