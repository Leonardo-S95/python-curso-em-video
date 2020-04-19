'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
'''

n1 = input('Digite algo aqui: ')

print('\033[1;33mO tipo primitivo é ', type(n1), '\033[m')

if n1.isnumeric() == True:
    print('\033[32mO que foi digitado é um número.\033[m')
else:
    print('\033[31mO que foi digitado não é um número.\033[m')

if n1.isalpha() == True:
    print('\033[32mO que foi digitado é alfabético.\033[m')
else:
    print('\033[31mO que foi digitado não é alfabético.\033[m')

if n1.isalnum() == True:
    print('\033[32mO que foi digitado é alfanumérico.\033[m')
else:
    print('\033[31mO que foi digitado não é alfanumérico.\033[m')

if n1.isspace() == True:
    print('\033[32mO que foi digitado é só espaço.\033[m')
else:
    print('\033[31mO que foi digitado não é só espaço.\033[m')

if n1.isupper() == True:
    print('\033[32mO que foi digitado contém somente letra maiúscula.\033[m')
else:
    print('\033[31mO que foi digitado não contém só letra maiúscula.\033[m')

if n1.islower() == True:
    print('\033[32mO que foi digitado contém somente letra minúscula.\033[m')
else:
    print('\033[31mO que foi digitado não contém só letra minúscula.\033[m')

if n1.istitle() == True:
    print('\033[32mO que foi digitado está capitalizado.\033[m')
else:
    print('\033[31mO que foi digitado não está capitalizado.\033[m')
