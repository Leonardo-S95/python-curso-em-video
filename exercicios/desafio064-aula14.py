'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles.
'''

print('Para sair, digite 999')

numero = int(input('Digite um número: '))
contador = 0
soma = 0

while numero != 999:
    soma += numero
    numero = int(input('Digite um número: '))
    contador += 1

print('Você digitou {} números, e a soma deles é {}.'.format(contador, soma))
