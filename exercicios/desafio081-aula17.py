'''
            DESAFIO 081
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
cont = 0
continuar = 'S'

while continuar[0] == 'S':
    lista.append(int(input(f'Digite o {cont + 1}º valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    cont += 1

print()
print(f'Foi(ram) digitado(s) {cont} número(s).')

lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
