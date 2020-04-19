'''
            DESAFIO 077
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('Ciencia', 'Computaçao', 'Macaco', 'Cachorro', 'Irineu', 'Relogio', 'Pikachu', 'Friends',
            'Celular', 'Astronauta')

cont = 0

for i in palavras:
    print(f'\n{i} tem a/as vogal/ais: ', end=' ')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
