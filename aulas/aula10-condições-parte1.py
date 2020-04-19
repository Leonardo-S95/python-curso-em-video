'''
tempo = int(input('Quantos anos tem seu carro?'))

if tempo <= 3:
    print('Carro novinho!')

else:
    print('Carro velhinho!')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #MESMA COISA QUE FOI FEITO ACIMA, SÓ QUE EM UMA LINHA.
tempo = int(input('Quantos anos teu seu carro?'))

print('Carro novo' if tempo <=3 else 'Carro velho')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nome = str(input('Qual é seu nome?')).strip().lower().split()
if nome[0] == 'leonardo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal.')
print('Bom dia/tarde/noite, {}!'.format(nome[0].capitalize()))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')

else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')     #Condição simplificada.

'''
            DESAFIO 028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

            DESAFIO 029
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

            DESAFIO 030
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

            DESAFIO 031
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
Km para viagens de até 200Km e R$0,45 para viagens mais longas.

            DESAFIO 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

            DESAFIO 033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

            DESAFIO 034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

            DESAFIO 035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
