'''
            DESAFIO 044
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format(' LOJAS XYZ '))          #^ significa centralizado. ^40 significa que será centralizado em
                                                #40 espaços.

preco = float(input('Digite o valor do produto: R$'))
opcao = int(input('\033[1;32m[ 1 ]\033[m Para pagamendo à vista no dinheiro/cheque e ganhe 10% OFF.\n'
                  '\033[1;32m[ 2 ]\033[m Para pagamento à vista no cartão e ganhe 5% OFF.\n'
                  '\033[1;32m[ 3 ]\033[m Para pagamento em 2x no cartão.\n'
                  '\033[1;32m[ 4 ]\033[m Para pagamento em 3x ou mais no cartão com 20% de juros.\n'
                  'Digite a opção de pagamento: '))

if opcao == 1:
    print('O valor do produto para pagamento à vista no dinheiro/cheque é de R${:.2f}.'.format(preco - (preco * 0.10)))
elif opcao == 2:
    print('O valor do produto para pagamento à vista no cartão é de R${:.2f}.'.format(preco - (preco * 0.05)))
elif opcao == 3:
    print('O valor de cada parcela será de R${:.2f}.'.format(preco / 2))
elif opcao == 4:
    parcelas = int(input('Deseja parcelar em quantas vezes?'))
    print('O valor de cada parcela será de R${:.2f}.'.format((preco + (preco * 0.2)) / parcelas))
else:
    print('Opção inválida. Tente novamente.')
