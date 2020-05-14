'''
            DESAFIO 096
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''


def área(larg, comp):
    print(f'A área de um terreno {l} x {c} é de {l * c}m²')


print('\n     CONTROLE DE TERRENOS     ')
print('-' * 30)
l = float(input('LARGURA (m): ').strip())
c = float(input('COMPRIMENTO (m): ').strip())

área(l, c)
