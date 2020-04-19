'''
            DESAFIO 022
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao tdo (sem considerar espaços);
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome todo maiúsculo é:', nome.upper())

print('Seu nome todo minúsculo é:', nome.lower())

nome_sem_espaco = nome.replace(' ', '')
print('O nome', nome, 'tem', len(nome_sem_espaco), 'letras.')    #Poderia ser: print('Seu nome tem ao tdo {}
                                                                 #letras.'.format(len(nome) - nome.count(' ')))
nomelista = nome.split()

print('O primeiro nome tem', len(nomelista[0]), 'letras.')       #Poderia ser: print('Seu primeiro nome
                                                                 #tem {} letras.'.format(nome.find(' ')))