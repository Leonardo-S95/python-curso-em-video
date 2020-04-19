'''
            DESAFIO 054
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores. (CONSIDERE A MAIORIDADE 21 ANOS)
'''

from datetime import date

year = date.today().year
maiores = 0
menores = 0

for i in range(0, 7):
    nasc = int(input('Digite o {}º ano de nascimento: '.format(i + 1)))
    if year - nasc >= 21:
        maiores += 1
    else:
        menores += 1

print('Dos anos de nascimento digitados, {} são maiores e {} são menores de idade.'.format(maiores, menores))
