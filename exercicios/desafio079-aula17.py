'''
            DESAFIO 079
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

continuar = 'S'
cont = 1
lista = []

while continuar == 'S':
    num = int(input(f'Digite o {cont}º número: '))
    cont += 1

    if num in lista:
        print('Número repetido não será adicionado.')
    else:
        lista.append(num)

    continuar = str(input('Deseja continuar? [S/N] ').upper())

lista.sort()

print('#-' * 30)
print(f'Você digitou os seguintes números: {lista}')
