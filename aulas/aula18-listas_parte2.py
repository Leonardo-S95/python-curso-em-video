'''
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

--------------------------------------------------------------------------

galera = [['João', 10], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for i in galera:
    print(f'{i[0]} tem {i[1]} anos de idade.')

'''

galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

'''
            DESAFIO 084
Faça um programa que leia nome e peso de vários pessoas, guardando tudo em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.

            DESAFIO 085
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
pares e ímpares em ordem crescente.

            DESAFIO 086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela, com a formatação correta. 

            DESAFIO 087
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.

            DESAFIO 088
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta.

            DESAFIO 089
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
'''