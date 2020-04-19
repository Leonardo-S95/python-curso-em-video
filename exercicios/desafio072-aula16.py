'''
            DESAFIO 072
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

opcao = 'S'

while opcao == 'S':
    escolha = int(input('Digite um número entre 0 e 20: '))

    while escolha < 0 or escolha > 20:
        escolha = int(input('Try again, stupid! Entre com um número entre 0 e 20: '))

    print(f'Você digitou o número {numeros[escolha]}.')
    opcao = input('Deseja continuar? [S/N] ')[0].strip().upper()
