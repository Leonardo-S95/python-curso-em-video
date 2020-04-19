'''
            DESAFIO 039
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

data = date.today().year

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = data - ano_nascimento
ano_alistamento = ano_nascimento + 18

if idade < 18:
    print('Seu alistamento será em {}.\nFalta(m) {} ano(s).'.format(ano_alistamento, ano_alistamento - data))

elif idade > 18:
    print('Você deveria ter se alistado há {} ano(s).\nSeu alistamento foi em {}.'.format(data - ano_alistamento,
                                                                                          ano_alistamento))

else:
    print('Você se alistará esse ano.')

'''
            #RESPOSTA NO VÍDEO
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual)
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano)
elif idade > 18:                #Também pode usar o else aqui.
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano)
'''