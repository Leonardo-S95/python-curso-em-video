'''
                DESAFIO 020
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada.
'''

from random import shuffle

nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem será: ')
print(lista)
