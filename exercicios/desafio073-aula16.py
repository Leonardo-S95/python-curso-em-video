'''
            DESAFIO 073
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time Chapecoense.
'''

futebol = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'Internacional', 'São Paulo',
           'Grêmio', 'Bahia', 'Athletico-PR', 'Atlético Mineiro', 'Botafogo', 'Goiás',
           'Vasco da Gama', 'Ceará', 'Fortaleza', 'Fluminense', 'Cruzeiro', 'CSA', 'Avaí',
           'Chapecoense')

print('===================================')
print(f'Lista de times do Brasileirão: \n{futebol}')
print('===================================')

print('Os 5 primeiros colocados são:')
for i in range(0, 5):
    print(futebol[i])
print('===================================')

print('Os 4 últimos colocados são:')
for i in range(-4, 0):
    print(futebol[i])
print('===================================')

print('Times em ordem alfabética: ')
print(sorted(futebol))
print('===================================')
print(f"O Chapeconese está na {futebol.index('Chapecoense') + 1}ª posição.")

'''
            RESPOSTA VÍDEO

times = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'Internacional', 'São Paulo',
           'Grêmio', 'Bahia', 'Athletico-PR', 'Atlético Mineiro', 'Botafogo', 'Goiás',
           'Vasco da Gama', 'Ceará', 'Fortaleza', 'Fluminense', 'Cruzeiro', 'CSA', 'Avaí',
           'Chapecoense')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
'''
