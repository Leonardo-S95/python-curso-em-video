'''
                DESAFIO 005
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
seu antecessor.
'''

print('\t\t\t\tDESCUBRA O SUCESSOR E O ANTECESSOR DE UM NÚMERO!')

n1 = int(input('Digite um número: '))
su = n1 + 1
an = n1 - 1

print('O sucessor de', n1, 'é \033[1;32m{}\033[m e o antecessor é \033[1;31m{}\033[m.'.format(su, an))
