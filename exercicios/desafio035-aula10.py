'''
            DESAFIO 035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

print('\t\tQUER SABER SE TRÊS RETAS CONSEGUEM FAZER UM TRIÂNGULO? VOCÊ ACHOU O PROGRAMA CERTO!!!')

n1 = float(input('Digite o valor da primeira reta aqui: '))
n2 = float(input('Digite o valor da segunda reta aqui: '))
n3 = float(input('Digite o valor da terceira reta aqui: '))

if abs(n2 - n1) < n1 < n2 + n3 and abs(n1 - n3) < n2 < n1 + n3 and abs(n1 - n2) < n3 < n1 + n2:
    print('É possível formar um triângulo com os valores dados.')

else:
    print('Não é possível formar um triângulo com os valores dados.')



'''
            #RESPOSTA NO VÍDEO

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')
'''