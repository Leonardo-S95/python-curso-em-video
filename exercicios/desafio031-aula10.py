'''
            DESAFIO 031
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

print('\t\tCALCULE O VALOR DE SUA PASSAGEM!!\nO valor é de R$0,50 por Km em distâncias de até 200Km. E R$0,45 para '
      'distâncias maiores que 200Km.')

dist = int(input('Digite a distância em Km que você percorrerá em sua viagem: '))

if dist <= 200:
    print('Foi cobrado R$0,50 por Km. O preço da sua passagem é de R${:.2f}'.format(dist * 0.50))

else:
    print('Foi cobrado R$0,45 por Km. O preço da sua passagem é de R${:.2f}'.format(dist * 0.45))


'''
            #RESPOSTA NO VÍDEO

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OU ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <=200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''