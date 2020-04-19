'''
            DESAFIO 049
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, q só que agora utilizando um laço for.
'''

print('\n{:*^40}\n'.format(' \033[4;36mNOVA TABUADA\033[m '))

n = int(input('Digite um número: '))

for i in range(0, 11):
    print('{} x {:2} = {}'.format(n, i, n * i))
