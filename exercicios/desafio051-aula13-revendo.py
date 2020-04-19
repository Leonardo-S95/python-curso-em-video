'''
            DESAFIO 051
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.


termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
an = termo + 10 * razao

print('Os 10 primeiros termos da PA com o primeiro número sendo {} e a razão sendo {} são:'.format(termo, razao))

for i in range(termo, an, razao):
    print(i)
'''

'''
            DESAFIO 051 (REFAZENDO)
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.


primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
an = primeiro + 10 * razao

for i in range(primeiro, an, razao):
    print(i)
'''

num = int(input('\nDigite o Primeiro número da PA: '))
razao = int(input('Digite a Razão da PA: '))

for c in range(0, 10):
    print(num, end=' → ')
    num += razao

print('ISSO É TUDO PESSOAL!')
