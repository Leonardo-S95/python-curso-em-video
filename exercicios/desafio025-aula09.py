'''
            DESAFIO 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
'''

name = str(input('Introduzca aquí su nombre: ')).strip().lower().split()

if 'silva' in name:
    print('Você tem Silva no nome.')

else:
    print('Você não tem Silva no nome.')


'''
            #RESPOSTA NO VÍDEO
            
nome = str(input('Qual é seu nome completo? ')).strip
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
'''