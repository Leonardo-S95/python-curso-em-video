'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
'''


numero = int(input('Um número digitar você deve: '))
opcao = 'S'
maior = numero
menor = numero
soma = 0
contador = 0

while opcao == 'S':
    soma += numero
    contador += 1

    if maior <= numero:
        maior = numero
    else:
        menor = numero

    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Opção inválida.\nDeseja continuar? [S/N] ')).upper().strip()

    if opcao == 'S':
        numero = int(input('Um número digitar você novamente deve: '))

print('A média entre todos os valores é {}, o maior número digitado foi {} e o menor foi {}.'.format(soma / contador, maior, menor))
