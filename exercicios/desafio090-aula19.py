'''
            DESAFIO 090
Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

dados = {}

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Qual a média de {dados["nome"]}: '))

print()

if dados['media'] >= 6:
    dados['situacao'] = 'aprovado'
else:
    dados['situacao'] = 'reprovado'

print(f'{dados["nome"]}, com média {dados["media"]}, foi {dados["situacao"]}.')
