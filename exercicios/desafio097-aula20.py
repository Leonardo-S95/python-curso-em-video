'''
            DESAFIO 097
Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva('Olá, Mundo!')
Saida: ~~~~~~~~~~~~
        Olá, Mundo!
       ~~~~~~~~~~~~
'''


def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


# Programa principal
escreva('Leonardo')
escreva('Oi')
escreva('AAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHH')
