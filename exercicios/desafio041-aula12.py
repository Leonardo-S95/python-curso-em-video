'''
            DESAFIO 041
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''

from datetime import date

data = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = data - ano

print('O atleta tem/terá {} anos em {}.'.format(idade, data))

if idade <= 9:
    print('Categoria: \033[1mMIRIM\033[m')

elif 14 >= idade > 9:
    print('Categoria: \033[1mINFANTIL\033[m')

elif 19 >= idade > 14:
    print('Categoria: \033[1mJUNIOR\033[m')

elif 25 >= idade > 19:
    print('Categoria: \033[1mSÊNIOR\033[m')

else:
    print('Categoria: \033[1mMASTER\033[m')


'''
            #RESPOSTA EM VÍDEO

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
'''