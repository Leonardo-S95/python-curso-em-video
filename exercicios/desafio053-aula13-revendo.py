'''
            DESAFIO 053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA; A SACADA DA CASA; A TORRE DA DERROTA; O LOBO AMA O BOLO; ANOTARAM A DATA DA MARATONA.


            #RESPOSTA NO VÍDEO

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')



            #OUTRA SOLUÇÃO

frase = srt(input('Digite a frase: ')).upper().strip().replace(' ', '')
if frase == frase[::-1]:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
'''

'''
            DESAFIO 053 (REFAZENDO)
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA; A SACADA DA CASA; A TORRE DA DERROTA; O LOBO AMA O BOLO; ANOTARAM A DATA DA MARATONA.
'''

frase = str(input('Escreva tua frase e descubra se ela é um palíndromo: ')).replace(' ', '').lower()

if frase == frase[::-1]:
    print('Sua frase é um lapin.. padri.. palíndromo.')
else:
    print("Sua frase não é um padin.. ladinpr..  FUCK THIS SHIT I'M OUT!")
