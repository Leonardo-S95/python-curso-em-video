'''
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche.append('cookie') adiciona o elemento ao final da lista
lanche.insert(0, 'cachorro quente') adiciona o elemento 'cachorro quente', na posição zero, nesse exemplo
del lanche[3] remove o item 3 da lista
lanche.pop(3) normalmente pop() é utilizado para eliminar o ultimo elemento, mas pode passar como parametro o indice
a ser eliminado
lanche.remove('pizza') remove() vc indica o valor e não o indice que quer eliminar

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() organiza em ordem crescente
valores.sort(reverse=True) organiza em ordem decrescente


num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
#num.pop(1)
num.remove(2)     # O remove() procura do inicio da lista, a primeira ocorrencia do valor que foi mandado eliminar, e elimina. NÃO ELIMINA TODOS OS VALORES
print(num)
print(f'Essa lista tem {len(num)} elementos.')


valores = []            #valores = list() é a mesma coisa
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for i, j in enumerate(valores):         #enumerate pega tanto a chave quanto o valor
    print(f'Na posição {i} encontrei o valor {j}...')

print(f'Fim da lista')
'''

a = [2, 3, 4, 7]
b = a[:]           #b = a faz com q o Python crie uma ligação de uma lista com a outra, algo alterado em uma lista, tbm é na outra
b[2] = 8           #b = a[:] faz com que o b receba uma cópia da lista a, sem ligação

print(f'Lista A: {a}')
print(f'Lista B: {b}')

'''
            DESAFIO 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.

            DESAFIO 079
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

            DESAFIO 080
Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta 
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

            DESAFIO 081
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.

            DESAFIO 082
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso. crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.

            DESAFIO 083
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a 
expressão passada está com os parênteses abertos e fechados na ordem correta.
'''