'''
            DESAFIO 067
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

n = c = 0

while True:
    n = int(input('Ver a tabuada de qual valor você quer? '))
    print('')
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n * c}')
        c += 1
    print('')
    c = 0

print("IT'S OVER!")
