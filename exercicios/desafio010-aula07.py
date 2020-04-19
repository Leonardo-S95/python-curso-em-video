'''
                DESAFIO 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar.
Considere US$1.00 == R$3.27
'''

print('\t\t\033[1;30;42m#~#CONVERSOR DE REAL PARA DOLAR#~#\033[m')

m = float(input('Digite sua graninha aqui: R$'))
d = m / 3.27

print('Com \033[32mR${:.2f}\033[m você consegue comprar \033[32mUS${:.2f}\033[m.'.format(m, d))