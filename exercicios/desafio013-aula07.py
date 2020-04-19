'''
                DESAFIO 013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento
'''

print('\t\033[30;41m~Ritual para ter muitos dinheiros... \033[m')

sal = float(input('Digite seu salário e magicamente ganhe um aumento: R$'))

aum = sal * 0.15
vf = sal + aum

print('Você ganhou um aumento de 15%!!! Seu salário foi de R${:.2f} para R${:.2f}.'.format(sal, vf))