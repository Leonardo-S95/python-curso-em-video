'''
            DESAFIO 106
Faça um mini-sistema que utilize o Interactive Help do Python, O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se
encerrará.
OBS: Use cores.
'''


def bgColor(txt, color=0):
    if color == 0:
        print(txt)
    elif color == 'yellow':
        print(f'\033[43m', txt, '\033[m')
    elif color == 'red':
        print(f'\033[41m', txt, '\033[m')
    elif color == 'blue':
        print(f'\033[44m', txt, '\033[m')
    elif color == 'white':
        print(f'\033[47m', txt, '\033[m]')


def linha(txt, color=0):
    if color == 'blue':
        bgColor('\033[30m-' * (len(txt) + 4), color)
        bgColor(f'\033[30m  {txt}', color)
        bgColor('\033[30m-' * (len(txt) + 4), color)
    else:
        bgColor('\033[36m-' * (len(txt) + 4), color)
        bgColor(f'\033[36m  {txt}', color)
        bgColor('\033[36m-' * (len(txt) + 4), color)


def intHelp():
    from time import sleep

    while True:
        linha('SISTEMA DE AJUDA PyHELP', color='yellow')
        print()
        sleep(.5)
        funcao = str(input('Função ou Biblioteca ~> ').strip())
        print()

        if funcao.upper() == "FIM":
            sleep(.5)
            linha('ADÍOOOOOOOOOOOOS!!!', color='blue')
            sleep(.5)
            quit()

        linha(f"Acessando o manual do comando '{funcao}'", color='red')
        sleep(1)
        print('\033[40m')
        help(funcao)
        print('\033[m')
        sleep(1)


intHelp()




'''

# SOLUÇÃO CURSO EM VÍDEO

from time import sleep

c = ('\033[m',          # 0 - Sem cores
     '\033[0;30,41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[7;30m'       # 6 - Branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca ~> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
'''
