'''
            DESAFIO 075
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primero valor 3.
c) Quais foram os números pares.
'''

cont = 1
lista = []

while cont <= 4:
    lista.append(int(input(f'Digite o {cont}º número: ')))
    cont += 1

cont = 0
numeros = tuple(lista)
lista.clear()

print(f'Os números digitados foram: {numeros}'.replace('(', '').replace(')', ''))
print(f'O número 9 apareceu {numeros.count(9)} vez(es).')

if 3 in numeros:
    print(f'O primeiro número 3 aparece na {numeros.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

while cont < len(numeros):
    if numeros[cont] % 2 == 0:
        lista.append(numeros[cont])
    cont += 1

print(f'Os números pares digitador foram: {lista}'.replace('[', '').replace(']', ''))
