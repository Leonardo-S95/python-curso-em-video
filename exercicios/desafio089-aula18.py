'''
            DESAFIO 089
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
'''

print('=-' * 30)
print('DADOS DE ALUNOS'.center(60))                 # FALTA CONSERTAR A TABELA
print('=-' * 30)
print()

dados = []
temp = []

while True:
    nome = str(input('Digite o nome do(a) aluno(a): ').strip().capitalize())
    temp.append(nome)
    for i in range(0, 2):
        temp.append(float(input(f'Digite a {i + 1}ª nota de {nome}: ').strip().replace(',', '.')))

    dados.append(temp[:])
    temp.clear()

    continuar = str(input('Deseja continuar? [S/N] ').upper().strip())

    if continuar[0] == 'N':
        print()
        break

print('#' * 26)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, j in enumerate(dados):
    print(f'{i:<4}', end='')
    print(f'{dados[i][0]:<10}', end='')
    print(f'{(dados[i][1] + dados[i][2]) / 2 :>8.1f}')

print()

while True:
    nota = int(input('Digite o número do aluno para ver suas notas: (666 para sair) ').strip())

    if nota == 666:
        print()
        print('-' * 30, 'FIM', '-' * 30)
        break

    print(f'As notas de {dados[nota][0]} são: {dados[nota][1]} e {dados[nota][2]}\n')
