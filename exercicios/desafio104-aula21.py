'''
            DESAFIO 104
Crie um programa que tenha um função chamada leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um
valor numérico.
Ex: n = leiaInt('Digite um nº: ')
'''


def leiaInt(txt):
    ok = False
    valor = 0

    while not ok:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n


# Programa principal
n = leiaInt('Digite um número: ')
print(f'O número {n} por você digitado foi.')
