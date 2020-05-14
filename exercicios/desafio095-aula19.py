'''
            DESAFIO 095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.

            DESAFIO 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

info = {}
jogador = []
gols = []
opcao = 'S'
count = total = outrocont = 0

while True:
    if opcao == 'N':
        break
    jogador.append(str(input('Digite su nombre: ')).title().strip())
    jogador.append(int(input(f'Digite quantas partidas {jogador[0]} jogou: ').strip()))

    while count < jogador[1]:
        gols.append((int(input(f'Quantos gols {jogador[0]} fez na {count + 1}ª partida? ').strip())))

        count += 1

    count = 0

    for i in range(0, len(gols)):
        total += gols[i]

    jogador.append(gols[:])
    jogador.append(total)
    gols.clear()

    total = 0

    info[outrocont] = jogador[:]
    jogador.clear()

    outrocont += 1

    opcao = str(input('Tens o que é necessário para continuardes? [S/N] '))[0].upper().strip()

outrocont = 0
print('=-' * 30)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total"}')
print('-' * 50)

for i in range(0, len(info)):
    print(f'{i:<4}{info[outrocont][0]:<15}{str(info[outrocont][2]):<20}{info[outrocont][3]}')

    outrocont += 1

opcao = 0
count = 1

while True:
    opcao = int(input('\nEntre com o código do jogador para ver seus dados: (999 para sair) ').strip())

    while opcao not in range(len(info)) and opcao != 999:
        opcao = int(input('Opção inválida. Entre com o código do jogador: '))

    if opcao == 999:
        break

    print(f'\n---------- Levantamento do jogador {info[opcao][0]}: ----------')

    for i in info[opcao][2]:
        print(f'No jogo {count} fez {i} gol(s).')

        count += 1

    count = 1
