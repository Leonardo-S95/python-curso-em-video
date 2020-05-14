'''
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal
título('    CURSO EM VÍDEO    ')
título('    PYTHON É MUITO BOM!    ')
título('    OI    ')
'''


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(b=4, a=5)
soma(7, 2)
print()


def contador(* num):             # * é o símbolo de desempacotar. Vai pegar um ou vários parâmetros e jogar dentro de num
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
print()


def soma(* numeros):
    s = 0
    for i in numeros:
        s += i
    print(f'Somando os valores {numeros} temos {s}.')


soma(5, 2)
soma(2, 9, 4)


'''
            DESAFIO 096
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.

            DESAFIO 097
Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como 
parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva('Olá, Mundo!')
Saida: ~~~~~~~~~~~~
        Olá, Mundo!
       ~~~~~~~~~~~~

            DESAFIO 098
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, 
fim e passos e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.

            DESAFIO 099
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

            DESAFIO 100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e 
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a 
segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''
