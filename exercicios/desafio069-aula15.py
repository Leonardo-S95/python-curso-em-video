'''
            DESAFIO 069
Crie um programa que leia a idade e o sexo de várias pesosas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''

idade = maiordeidade = homem = mulher = 0
sexo = ''
continuar = 'S'

print('=-=' * 10)
print('     CU - Cadastro Único')
print('=-=' * 10, '\n')

while continuar == 'S':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite novamente o sexo: [M/F]')).strip().upper()[0]
    if idade > 18:
        maiordeidade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite novamente se deseja continuar: [S/N]')).strip().upper()[0]

print('\n===== THE END DO PROGRAMA =====\n')
print(f'Total de pessoas com +18 anos: {maiordeidade}')
print(f'{homem} homem(ns) foi(ram) cadastrado(s).')
print(f'{mulher} mulher(es) com menos de 20 anos foi(ram) cadastrada(s).\n')
