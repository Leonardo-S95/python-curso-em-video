'''
            DESAFIO 055
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i + 1)))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('A pessoa de maior peso pesa {:.1f}kg e a de menor peso pesa {:.1f}kg.'.format(maior, menor))
