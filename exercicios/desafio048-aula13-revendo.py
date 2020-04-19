'''            DESAFIO 048
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo entre 1 e 500.


soma = 0
cont = 0

for i in range(3, 501, 3):
    if i % 2 != 0:
        cont = cont + 1                 #cont = cont + 1 é a mesma coisa que cont += 1
        soma = soma + i                 #soma = soma + i é a mesma coisa que soma += i

print('A soma dos {} valores é igual a {}.'.format(cont, soma))




            #RESPOSTA NO VÍDEO
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
        
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
'''

'''            DESAFIO 048 (REFAZENDO)
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo entre 1 e 500.
'''

soma = 0

for i in range(3, 501, 3):
    if i % 2 != 0:
        soma += i

print(soma)
