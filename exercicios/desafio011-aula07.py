'''
                DESAFIO 011
Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de
tinta pinta uma área de 2m²
'''

larg = float(input('\033[34mDigite a largura de sua parede:\033[m '))
alt = float(input('\033[34mDigite a altura de sua parede:\033[m '))

area = larg * alt

tinta = area / 2

print('Sua parede tem {:.2f}m² e você precisará de \033[4;30m{:.2f}\033[m litros de tinta para pintá-la.'
      .format(area, tinta))