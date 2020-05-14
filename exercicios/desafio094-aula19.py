'''
            DESAFIO 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média
'''

dados = []
temp = {}
mulheres = []
acimamedia = []
soma = media = 0

print()

while True:
    nome = str(input('Caso deseje encerrar o programa, digite PNEUMOULTRAMICROSCOPICOSSILICOVULCANOCONIÓTICO.\nNome: ')).strip().title()

    if nome == 'Pneumoultramicroscopicossilicovulcanoconiótico':
        break

    temp['nome'] = nome
    temp['sexo'] = str(input('Sexo: [M/F] '))[0].strip().upper()

    while temp['sexo'][0] != 'M' and temp['sexo'][0] != 'F':
        temp['sexo'] = str(input('Opção inválida! Digite "M" para masculino ou "F" para feminino: ')).strip().upper()

    if temp['sexo'] == 'F':
        mulheres.append(temp['nome'])

    temp['idade'] = int(input('Idade: '))

    dados.append(temp.copy())

for i in dados:
    soma += i['idade']

if len(dados) > 0:
    media = soma / len(dados)

for i in dados:
    if i['idade'] > media:
        acimamedia.append(i)

print('=' * 70)
print(f'Foi(ram) cadastrada(s) ', len(dados), 'pessoa(s).')

if len(dados) > 0:
    print(f'A média de idade das pessoas é: {media:.2f} anos.')
else:
    print('Não dá pra calcular a média de ninguém, né. Dãããa..')

if len(mulheres) != 0:
    print('Mulheres cadastradas: ', end='')

    for i in range(0, len(mulheres)):
        if i == len(mulheres) - 1:
            print(f'{mulheres[i]}.')
            break
        print(mulheres[i], end=', ')

if len(acimamedia) !=0:
    print('Pessoas com idade acima da média: ', end='')

    for i in range(0, len(acimamedia)):
        if i == len(acimamedia) - 1:
            print(f'{acimamedia[i]["nome"]}.')
            break
        print(acimamedia[i]["nome"], end=', ')
