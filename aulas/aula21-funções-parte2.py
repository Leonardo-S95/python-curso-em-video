'''
    > > > Interactive Help < < <
help()    <~ aceita uma função dentro dos () para mostrar uma explicação sobre.
Para sair digite quit
print(umafunção.__doc__)    <~   mostra uma explicacão da função.


    > > > Docstrings < < <
Coloque aspas duplas após definir uma função para criar uma docstring, um manual da função.


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i

    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)


    > > > Parâmetro opcional < < <


def somar(a=0, b=0, c=0):            # colocando o =0, caso a função não receba um valor para a ou/e b ou/e c, o valor será 0 e a função funcionará.
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)
somar()
somar(c=3, a=2)


    > > > Escopo de variáveis < < <


def teste():
    x = 8               # x é uma variável local, tem um escopo local, só vai funcionar dentro do def
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2                   # n é uma variável global, tem um escopo global
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')         # Vai dar erro no programa, já que o x é uma variável local.

teste()
-------------------------------------------------------------------------------------


def teste(b):
    global a            # vai mudar a variável 'a' global de 5 para 8
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}.')


    > > > Retornando valores (return) < < <


def somar (a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3= somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}.')
'''

def fatorial(num=1):
    f = 1           # variável local
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
print()
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

'''
            DESAFIO 101
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano 
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

            DESAFIO 102
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

            DESAFIO 103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar o ficha do jogador, mesmo que algum dado não tenha 
sido informado corretamente.

            DESAFIO 104
Crie um programa que tenha um função chamada leiaInt(), que vai funcionar de forma 
semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um 
valor numérico.
Ex: n = leiaInt('Digite um nº: ')

            DESAFIO 105
Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos 
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.

            DESAFIO 106
Faça um mini-sistema que utilize o Interactive Help do Python, O usuário vai digitar o 
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se 
encerrará.
OBS: Use cores.
'''
