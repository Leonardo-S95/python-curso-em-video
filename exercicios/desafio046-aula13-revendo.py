'''
            DESAFIO 046
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.


from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('')
print('\t\033[30;41m~LE FOGOS DE ARTIFÍCIOS EXPLODINDO! FIIIUM, FIIIUM, KABUM, KATCHIAU, FIIIUM, BUM!!!\033[m')
'''

'''            DESAFIO 046 (REFAZENDO)
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
'''

from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('XABLAU!')