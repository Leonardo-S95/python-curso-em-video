'''
Crie um programa que leia dois números e mostre a soma entre eles.
'''
print('\tCALCULADORA\n')
n1 = int(input('Digite um número aqui: '))
n2 = int(input('Digite outro número aqui: '))
s = n1 + n2

cores = {'boldbranco': '\033[1;30m',
         'underlineverde': '\033[4;32m',
         'limpa': '\033[m'}

print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['boldbranco'], n1, cores['limpa'],
                                                              cores['boldbranco'], n2, cores['limpa'],
                                                              cores['underlineverde'], s, cores['limpa']))