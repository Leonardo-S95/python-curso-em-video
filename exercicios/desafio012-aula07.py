'''
                DESAFIO 012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
5% de desconto.
'''

print('\t\033[30;46m~~~~~~~~DESCONTÃO PRA ACABAR COM O ESTOQUE~~~~~~~~\033[m')

p = float(input('Digite o preço para receber o desconto: R$'))

d = p * 0.05
vf = p - d

print('Seu produto foi de R${:.2f} para R$\033[32m{:.2f}\033[m.'.format(p, vf))