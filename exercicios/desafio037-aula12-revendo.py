'''
            DESAFIO 037
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

print('             \033[1;34;40m~~~ CONVERSOR NUMÉRICO ~~~\033[m')

escolha = int(input('\033[1mDeseja fazer a conversão para qual base?'
                    '\n[ 1 ] para binário.'
                    '\n[ 2 ] para octal.'
                    '\n[ 3 ] para hexadecimal.'
                    '\nDigite a opção desejada: \033[m'))

num = int(input('Digite o número para ser convertido: '))

if escolha == 1:
    print('Transformando {} em binário fica {}.'.format(num, bin(num)[2:]))

elif escolha == 2:
    print('Transformando {} em octal fica {}.'.format(num, oct(num)[2:]))

elif escolha == 3:
    print('Transformando {} em hexadecimal fica {}.'.format(num, hex(num)[2:].upper()))

else:
    print('Opção inválida.')
