'''
            DESAFIO 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

dados = {}
gol = []
count = 0
total = 0

dados['nome'] = str(input('Entre com o nome do jogador: '))
dados['partidas'] = int(input(f'Digite quantas partidas {dados["nome"]} jogou: '))

while count < dados['partidas']:
    temp = int(input(f'Quantos gols {dados["nome"]} fez na {count + 1}ª partida? '))
    gol.append(temp)
    total += temp
    count += 1

dados['total'] = total
dados['gol'] = gol[:]
gol.clear()

print('♫' * 40)

for i, j in dados.items():
    print(f'O campo {i} tem o valor de {j}.')

print('♫' * 40)

for i in range(0, dados['partidas']):
    print(f'Na partida {i + 1}, fez {dados["gol"][i]} gol(s).')

print(f'Total de {dados["total"]} gol(s).')
