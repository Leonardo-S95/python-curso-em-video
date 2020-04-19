'''
            DESAFIO 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo'.
'''

cidade = str(input('Digite o nome de sua city: ')).lower().strip()

cidadesplit = cidade.split()

if 'santo' in cidadesplit[0]:
    print('Sua cidade começa com Santo.')

else:
    print('Sua cidade não começa com Santo.')


'''
            #RESPOSTA NO VÍDEO
            
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
'''