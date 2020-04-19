'''
            DESAFIO 087
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''

matriz = [[], [], []]
spar = ster = maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Entre com um número para a posição {[i]}{[j]}: ')))

        if matriz[i][j] % 2 == 0:           # SOMA DOS VALORES PARES
            spar += matriz[i][j]

        if j == 2:                          # SOMA DOS VALORES DA TERCEIRA COLUNA
            ster += matriz[i][j]

        while i == 1:                       # MAIOR VALOR DA SEGUNDA LINHA
            if j == 0:
                maior = matriz[i][j]
                break
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                break
            break

for i in range(0, 3):
    print()
    for j in range(0, 3):
        print(f'[  {matriz[i][j]:^5}  ]', end='')

print('\n')
print(f'A soma de todos os valores pares digitados é: {spar}.')
print(f'A soma dos valores da terceira coluna é: {ster}.')
print(f'O maior valor da segunda linha é: {maior}.')
