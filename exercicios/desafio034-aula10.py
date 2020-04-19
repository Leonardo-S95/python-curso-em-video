'''
            DESAFIO 034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

print('\t\tVENHA RECEBER UM AUMENTO DO NADA!!')

sal = float(input('Digite seu salário: R$'))

if sal > 1250:
    print('Você recebeu um aumento de 10%. Seu salário atual é de R${:.2f}'.format((sal * 0.10) + sal))

if sal <= 1250:
    print('Você recebeu um aumento de 15%. Seu salário atual é de R${:.2f}'.format((sal * 0.15) + sal))



'''
            #RESPOSTA NO VÍDEO

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
'''