'''
            DESAFIO 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.


lista = []

for cont in range(0, 5):
    lista.append(int(input('Digite um número: ')))

print(f'O maior valor digitado foi {max(lista)} na posição ', end='')

for x in range(0, len(lista)):
    if lista[x] == max(lista):
        print(f'{x}', end=', ')

print('\n')
print(f'O menor valor digitado foi {min(lista)} na posição ', end='')

for y in range(0, len(lista)):
    if lista[y] == min(lista):
        print(f'{y}', end=', ')
'''

#RESPOSTA CURSO EM VIDEO
lista = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')

print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()
