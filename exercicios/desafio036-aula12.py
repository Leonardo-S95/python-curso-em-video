'''
            DESAFIO 036
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

print('\033[33m=\033[m' * 60)
print('\t\t\t\033[32mPROGRAMA PARA EMPRESTIMO BANCÁRIO\033[m')
print('\033[33m=\033[m' * 60)

valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
anos = int(input('Digite em quantos anos você pretende pagar: '))

anos_meses = anos * 12
prestacao_mensal = valor_casa / anos_meses
salario30 = salario * 0.30

if prestacao_mensal <= salario30:
    print('Empréstimo aprovado! O valor da prestação será de: R${:.2f}'.format(prestacao_mensal))
else:
    print('Infelizmente o empréstimo foi negado devido a prestação mensal, com valor'
          ' de R${:.2f}, ultrapassar 30% do seu salário.'.format(prestacao_mensal))