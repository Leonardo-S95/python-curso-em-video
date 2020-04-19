'''
                DESAFIO 009
Faça um programa que leia um número inteiro qualquer e mostre sua tabuada.
'''

print('\t~~~TABUADA~~~')

n1 = int(input('Digite um número aqui: '))

m0 = n1 * 0
m1 = n1 * 1
m2 = n1 * 2
m3 = n1 * 3
m4 = n1 * 4
m5 = n1 * 5
m6 = n1 * 6
m7 = n1 * 7
m8 = n1 * 8
m9 = n1 * 9
m10 = n1 * 10

print('\033[1;36m{} x 0 = {}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}'
      '\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}\033[m'
      .format(n1, m0, n1, m1, n1, m2, n1, m3, n1, m4, n1, m5, n1, m6, n1,
              m7, n1, m8, n1, m9, n1, m10))

'''
Como as variáveis m0, m1, m2, ..., m10 não serão usadas no futuro, é possível fazer
desse jeito abaixo.

print('\t~~~TABUADA~~~')

n = int(input('Digite um número aqui: '))
print('-' * 12)
print('{} x {:2} = {}'.format(n, 0, n*0))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-' * 12)

OBS: O ":2" dentro da segunda chave é para deixar alinhado o sinal de igual,
     por que o programa vai considerar que os números "0, 1, 2, 3, ..., 9" 
     tem 2 casas, igual o 10.
'''