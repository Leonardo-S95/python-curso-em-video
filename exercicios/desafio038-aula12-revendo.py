'''
            DESAFIO 038
Escreva um programa que leia dois números inteiros e compare-os, mostrando
na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

print('\033[1;31;40m¨¨¨¨ Már grande ou már pequeno ou merma coisa ¨¨¨¨\033[m')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O number {} is maior que o número {}.'.format(num1, num2))

elif num2 > num1:
    print('O número {} é mais maior de grande que o número {}.'.format(num2, num1))

else:
    print('Merma coisa.')