'''
            DESAFIO 037
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

print('\033[36m~=~\033[m' * 20)
print('\t\t\t\033[31mCONVERSÃO DE BASE NUMÉRICA\033[m')
print('\033[36m~=~\033[m' * 20)

num = int(input('Digite um número inteiro: '))
conversao = int(input('Escolha uma das bases que você deseja.\nDigite 1 para binário;\nDigite 2 para octal;\n'
                      'Digite 3 para hexadecimal.\nSua opção: '))

if conversao == 1:
    print('O número {} em \033[1mBINÁRIO\033[m é {}'.format(num, bin(num)[2:]))
elif conversao == 2:
    print('O número {} em \033[1mOCTAL\033[m é {}'.format(num, oct(num)[2:]))
elif conversao == 3:
    print('O número {} em \033[1mHEXADECIMAL\033[m é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')