'''
                DESAFIO 007
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a
sua média.
'''


print('\t\t\t\tDescubra sua média!')

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite mais uma nota: '))
m = (n1 + n2) / 2

print('Sua média é: \033[7m{:.1f}\033[m'.format(m))