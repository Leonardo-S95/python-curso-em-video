'''
            DESAFIO 092
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de
ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime

dados = {}

dados['nome'] = str(input('Digite seu nome: '))
dados['idade'] = datetime.now().year - int(input('Digite seu ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho: (0 caso não tenha) '))

for i, j in dados.items():
    if dados['ctps'] == 0:
        print('=-' * 30)
        for k, l in dados.items():
            print(f'{k} tem o valor de {l}')
        quit()

dados['contratacao'] = int(input('Ano de contratação: '))
dados['salario'] = float(input('Qual seu salário: R$ '))
dados['aposentadoria'] = (35 - (datetime.now().year - dados['contratacao'])) + dados['idade']

print('=-' * 30)

for i, j in dados.items():
    print(f'{i} tem o valor de {j}')
