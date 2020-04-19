'''
            DESAFIO 061
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
a estrutura while.

            DESAFIO 051
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
'''

n = int(input('Digite o PRIMEIRO TERMO da PA: '))
r = int(input('Digite a RAZÃO da PA: '))
t = 1

print('Os dez primeiros termos da PA são: ')

while t <= 10:
    if t == 1:
        print(n)
        t += 1
    else:
        n += r
        print(n)
        t += 1


'''
            #RESPOSTA NO VÍDEO
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
'''