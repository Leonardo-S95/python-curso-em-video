'''
            DESAFIO 033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

print('~' * 9, 'QUAL DOS TRÊS NÚMEROS É O MAIOR?', '~' * 9)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 == n2 == n3:
    print('Os três números digitados são iguais.')

if n1 > n2 and n1 > n3:
    print('{} é o maior número.'.format(n1))

if n2 > n1 and n2 > n3:
    print('{} é o maior número.'.format(n2))

if n3 > n1 and n3 > n2:
    print('{} é o maior número.'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor número.'.format(n1))

if n2 < n1 and n2 < n3:
    print('{} é o menor número.'.format(n2))

if n3 < n1 and n3 < n2:
    print('{} é o menor número.'.format(n3))


'''
            #RESPOSTA NO VÍDEO

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é menor
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior
maior = a
if b > a and b > c:
    menor = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
'''