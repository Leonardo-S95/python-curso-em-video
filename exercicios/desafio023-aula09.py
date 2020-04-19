'''
            DESAFIO 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

num = input('Digite um número entre 0 e 9999: ')

if len(num) == 1:
    print('''Unidade: {}
Dezena: -
Centena: -
Milhar: -'''.format(num[0]))

if len(num) == 2:
    print('''Unidade: {}
Dezena: {}
Centena: -
Milhar: -'''.format(num[1], num[0]))

if len(num) == 3:
    print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: - '''.format(num[2], num[1], num[0]))

if len(num) == 4:
    print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(num[3], num[2], num[1], num[0]))

if len(num) > 4:
    print('Seu puto, o número tem que ter até 4 digitos.\nPARA DE ESTRAGAR MEU PROGRAMA!')


'''
            #RESPOSTA NO VÍDEO
            
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))
'''