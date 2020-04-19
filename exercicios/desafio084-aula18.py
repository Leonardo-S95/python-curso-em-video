'''
            DESAFIO 084
Faça um programa que leia nome e peso de vários pessoas, guardando tudo em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.

dados = []
maior = []
menor = []
count = 0

while True:
    count += 1
    nome = (str(input(f'NOME da {count}ª pessoa: ').strip()))
    dados.append(nome)
    dados.append(float(input(f'PESO de {nome}: ').replace(',', '.')))

    if dados[1] <= 70:
        menor.append(dados[0])
    elif dados[1] >= 100:
        maior.append(dados[0])

    dados.clear()

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if continuar[0] == 'N':
        break

print(f'Foram cadastradas {count} pessoas.\nO maior peso foi de 100Kg pra cima: {maior}\nO menor peso foi de 70Kg pra baixo: {menor}')
'''

temp = []
dados = []
maior = menor = 0
count = 0

while True:
    count += 1
    nome = (str(input(f'NOME da {count}ª pessoa: ').strip()))
    temp.append(nome)
    temp.append(float(input(f'PESO de {nome}: ').replace(',', '.')))

    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    dados.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if continuar[0] == 'N':
        break

print('=-' * 30)
print(f'Foram cadastradas {count} pessoas.')
print(f'O maior peso foi {maior}Kg: ', end='')

for i in dados:
    if i[1] == maior:
        print(f'{i[0]} ', end='')

print(f'\nO menor peso foi {menor}Kg: ', end='')

for i in dados:
    if i[1] == menor:
        print(f'{i[0]} ', end='')

print()
