'''
            DESAFIO 029
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

print('-' * 10 + 'Consulte se você está na velocidade permitida!' + '-' * 10)

velo = int(input('Digite sua velocidade em Km/h: '))

if velo > 80:
    print('Você foi multado! O limite permitido é de 80Km/h.')
    print('O valor de sua multa é: R${:.2f}'.format((velo - 80) * 7))

else:
    print('Você está dentro do limite de velocidade permitido!')


'''
            #RESPOSTA NO VÍDEO
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
'''