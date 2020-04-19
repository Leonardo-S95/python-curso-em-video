'''                DESAFIO 008
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milímetros.
'''

print('\t\t\t\tTransforme metros em centímetros e milímetros!')
n1 = float(input('Digite um valor em metros: '))

c = n1 * 100
m = n1 * 1000

print('\033[1;30m{} metros para centímetros =\033[m \033[1;33m{}\033[m\n\033[1;30m{} metros para milímetros =\033[m'
      '\033[1;33m {}\033[m'.
      format(n1,c,n1,m))