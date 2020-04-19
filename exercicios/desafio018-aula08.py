'''
                DESAFIO 018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo para descobrir o seno, cosseno e tangente: '))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('O ângulo de {}º tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(angulo, sen, cos, tan))