'''
            DESAFIO 042
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

print('\t\tQUER SABER SE TRÊS RETAS CONSEGUEM FAZER UM TRIÂNGULO? VOCÊ ACHOU O PROGRAMA CERTO!!!')

n1 = float(input('Digite o valor da primeira reta aqui: '))
n2 = float(input('Digite o valor da segunda reta aqui: '))
n3 = float(input('Digite o valor da terceira reta aqui: '))

if abs(n2 - n1) < n1 < n2 + n3 and abs(n1 - n3) < n2 < n1 + n3 and abs(n1 - n2) < n3 < n1 + n2:
    print('É possível formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO.')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO.')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:     #else também funcionaria.
        print('ISÓSCELES.')

else:
    print('Não é possível formar um triângulo com os valores dados.')

