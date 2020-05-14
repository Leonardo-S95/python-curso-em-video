'''
dados = {'nome': 'Pedro', 'idade': 25}          # dados = dict{} é a mesma coisa

print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'    # Criação do elemento 'sexo' e adicionando 'M'. Dicionário não usa append.

print(dados['sexo'])

del dados['idade']      # Remove o elemento 'idade'.

print(dados)

-----------------------------------------------------------------------------

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values())       # Mostra os valores. No caso = Star Wars, 1977...
print(filme.keys())         # Mostra as chaves. No caso = titulo, ano...
print(filme.items())        # Mostra os valores e as chaves.
print()

for k, v in filme.items():
    print(f'O {k} é {v}.')
print()


locadora = []

locadora.append(filme)             # Colocando o dicionário dentro de uma lista.

print(locadora[0]['ano'])
print(locadora[0]['titulo'])

-----------------------------------------------------------------------------------

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e o sexo é {pessoas["sexo"]}.\n')

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')

---------------------------------------------------------------------------------

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())        # É como se fosse o [:] das listas

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

'''
            DESAFIO 090
Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.

            DESAFIO 091
Crie um programa onde 4 jogadores jogue um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em 
ordem, sabendo que o vencedor tirou o maior número no dado.

            DESAFIO 092
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de 
ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule 
e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

            DESAFIO 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

            DESAFIO 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os 
dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média

            DESAFIO 095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo 
um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
