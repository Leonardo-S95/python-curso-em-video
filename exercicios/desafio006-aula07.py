'''
                DESAFIO 006
Crie um algoritmo que leia um número e mostre o seu dobre, tripo e raiz quadrada.
'''

n1 = int(input('Digite um número aqui: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

color = {'boldazul': '\033[1;34m',
         'boldbranco': '\033[1;30m',
         'limpa': '\033[m'}
print('O dobro de {}{}{} é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{:.2f}{}.'.format(color['boldbranco'], n1,
                                                                                             color['limpa'],
                                                                                             color['boldazul'], d,
                                                                                             color['limpa'],
                                                                                             color['boldazul'], t,
                                                                                             color['limpa'],
                                                                                             color['boldazul'], r,
                                                                                             color['limpa']))

# função pow também faz potência.
# Ex print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(n1, (n1*2), (n1*3), pow(n1, (1/2))))