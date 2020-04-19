'''
            DESAFIO 060
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
'''

            #FATORIAL USANDO O WHILE

print('\033[33m=-=\033[m' * 15)
print('\033[36m{:^45}\033[m'.format('CALCULADORA DE FATORIAL'))
print('\033[34m=-=\033[m' * 15)

n = int(input('Digite um número para saber seu fatorial: '))
cont = n
fatorial = 1

while cont > 1 and cont != 0:
    fatorial *= cont * (cont - 1)
    cont -= 2
print('O fatorial de {} é igual a {}.'.format(n, fatorial))

'''
            #FATORIAL USANDO O FOR

n = int(input('Digite um número para saber seu fatorial: '))
cont = n
fatorial = 1

for i in range(n, 1, -1):
    fatorial *= cont
    cont -= 1
print('{}! é igual a {}.'.format(n, fatorial))



            #RESPOSTA NO VÍDEO
n = int(input('Digite um número para calcular sau fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''