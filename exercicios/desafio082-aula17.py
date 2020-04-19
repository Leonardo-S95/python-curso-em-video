'''
            DESAFIO 082
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso. crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
par = []
impar = []
count = 0
continuar = 'S'

while continuar[0] == 'S':
    lista.append(int(input(f'Digite o {count + 1}º valor: ')))
    continuar = str(input('Vossa Excelência desejas continuardes? [S/N] ')).upper().strip()
    count += 1

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])

print()
print('=-' * 30)
print(f'A lista completa contém os seguintes números: {lista}.')
print(f'~le números pares da lista são: {par}.')
print(f'Os numeritos imparitos da listita son: {impar}.')
print('=-' * 30)
