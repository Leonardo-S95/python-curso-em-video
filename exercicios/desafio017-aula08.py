'''
                DESAFIO 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
'''

print('\033[7;30m~~~~~~AGORA SEUS PROBLEMAS PARA DESCOBRIR A HIPOTENUSA ACABARAM!!~~~~~~\033[m\t\t\t\t\t Eu acho')

from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

print('A hipotenusa será: {:.2f}'.format(hypot(co, ca)))