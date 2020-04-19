'''
            DESAFIO 050
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.


soma = 0
cont = 0

for i in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1

print('Você informou {} números pares e a soma entre eles é igual a {}.'.format(cont, soma))
'''

'''
            DESAFIO 050 (REFAZENDO)
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''

soma = 0
n = 0

for i in range(0, 6):           #OPS.. FIZ DE NÚMERO ÍMPAR, MAS TÁ VELENDO.
    n = int(input('Digite o {}º número: '.format(i+1)))
    if n % 2 != 0:
        soma += n

print('A soma dos números ímpares é = {}'.format(soma))
