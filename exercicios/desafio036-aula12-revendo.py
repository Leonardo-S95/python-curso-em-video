'''
            DESAFIO 036
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado.
'''

print('\033[32;46m #^#^# CONSIGA SEU EMPRÉSTIMO #^#^# \033[m')

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos você pretende pagar? '))*12

prestacao = casa/anos

if salario * (30/100) > prestacao:
    print('O empréstimo foi aprovado. A prestação será de R${:.2f}'
          ' durante {:.0f} anos.'.format(prestacao, anos/12))

else:
    print('Empréstimo negado! Para o seu empréstimo ser aprovado, a prestação'
          ' não pode exceder 30% do seu salário.'
          '\nPrestação = R${:.2f}'
          '\n30% do salário = R${:.2f}'.format(prestacao, salario * (30/100)))
