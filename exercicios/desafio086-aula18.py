'''
            DESAFIO 086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um número para a posição {[i]}{[j]}: ')))

for i in range(0, 3):
    print()
    for j in range(0, 3):
        print(f'[  {matriz[i][j]:^5}  ]', end='')

print()


# SOLUÇÃO CURSO EM VÍDEO
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''
