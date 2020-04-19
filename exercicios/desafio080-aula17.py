'''
            DESAFIO 080
Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []
cont = 0

for i in range(0, 5):
    num = int(input(f'Digite o {cont + 1}º valor: '))

    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('O número foi adicionado ao final da lista.')
    else:
        for i in range(0, 5):
            if num <= lista[i]:
                lista.insert(i, num)
                print(f'O número foi adicionado na posição {i}')
                break

    cont += 1

print(lista)
