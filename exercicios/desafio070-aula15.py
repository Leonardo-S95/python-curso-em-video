'''
            DESAFIO 070
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000,.
c) Qual é o nome do produto mais barato.
'''

nome = ''
nomebarato = ''
preco = maisbarato = total = maisdemil = contador = 0
continuar = 'S'

while continuar == 'S':
    nome = str(input('Produto: '))
    preco = float(input('Valor: R$ '))
    total += preco

    if contador == 0:
        maisbarato = preco
        contador += 1
    if preco > 1000:
        maisdemil += 1
    if maisbarato >= preco:
        nomebarato = nome
        maisbarato = preco

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    while continuar not in 'SN':
        continuar = input('Opção inválida! Deseja continuar? [S/N]').strip().upper()[0]

print('\n===== FIM DO PROGRAMA =====\n')
print(f'O total da compra foi de R${total:.2f}.\n'
      f'Temos {maisdemil} produto(s) custando mais de R$1000,00.\n'
      f'O produto mais barato foi {nomebarato}, custando R${maisbarato:.2f}.')
