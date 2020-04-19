'''
                    ###SOBRE FATIAMENTO###

frase = 'Curso em vídeo Python'   #0 é o C, 1 u, 2 r, 3 s, 4 o, 5 (espaço), 6 e, 7 m, 8 (espaço), 9 v, 10 í, 11 d, 12 e,
                                  #13 o, 14 (espaço), 15 P, 16 y, 17 t, 18 h, 19 o, 20 n.

print(frase[9:13])         # Vai do 9 até o 13, sendo que o 13 não entra na contagem. O último valor não entra na contagem.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase[9:21:2])        # Vai do 9 até o 21, pulando de 2 em 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase[:5])            #Quando não tem o primeiro valor, é a mesma coisa que escrever o 0.
                            #O Python entende que é do inicio. Ou seja, nesse caso é [0:5].
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase[15:])           #Não colocando o final indica pro Python que quero do 15 até o final.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase[9::3])          #Começa no 9 e como não tem o segundo número, vai até o final. O 3 quer dizer que vai pulando
                            #de 3 em 3 casas.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                ###SOBRE ANÁLISE###



frase = 'Curso em Vídeo Python'

print(len(frase))            #len vem de length, que significa comprimento.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.count('o'))      #Nesse caso count contará quantas vezes aparece a letra 'o' minúscula. Tem diferença de
                             #letra maiúscula e minúscula.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.count('o', 0, 13))      #Nesse caso ele vai considerar do 0 até o 13 (lembrando que o 13 não será incluído).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.find('deo'))            #Ele vai mostrar em que momento começou o 'deo'.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.find('Vídeo'))          #Ele mostra a posição que começa a palavra procurada, caso exista.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.find('Android'))        #Se você coloca no find uma string que não exista, ele te retorna o valor -1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print('Curso' in frase)             #O operado in vai dizer se existe 'Curso' na variável frase, retornando True para
                                    #caso exista e False para caso não exista.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ###SOBRE TRANSFORMAÇÃO###

frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))       #Nesse caso o replace substituiria a palavra 'Python' por 'Android' no
                                                #momento que foi pedido.
                                                #Uma string em seus microelementos é IMUTÁVEL, a não ser que eu utilize
                                                #uma função de transformação de string e faça uma atribuição.
                                                #Ex: frase = frase.replace('Python', 'Android')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.upper())                #O que já for maiúsculo ele mantém, o que não for ele coloca maiúsculo.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.lower())                #O que já for minúsculo ele mantém, o que não for ele coloca minúsculo.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.capitalize())           #O capitalize vai jogar todos os caracteres para minúsculo e só o primeiro
                                    #caracter ficará maiúsculo.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.title())                #O title vai colocar o primeiro caracter de cada palavra maiúsculo.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = '   Aprenda Python  '

print(frase.strip())                #strip removerá todos os espaços inúteis no início e no final da string.
                                    #O espaço do meio será mantido.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = '   Aprenda Python  '

print(frase.rstrip())               #rstrip removerá somente os espaços inúteis da direita, os últimos espaços.
                                    #rstrip, o r significa right. Muitas funções no Python tem a variação r.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = '   Aprenda Python  '

print(frase.lstrip())               #lstrip removerá somente os espaços inúteis da esquerda, os primeiros espaços.
                                    #lstrip, o l significa left.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ###SOBRE DIVISÃO###

frase = 'Curso em Vídeo Python'

print(frase.split())                #Vai ocorrer uma divisão na sua string considerando os espaços.
                                    #O split gera uma lista com todas as palavras de um cadeia de caracteres.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ###SOBRE JUNÇÃO###

frase = 'Curso em Vídeo Python'

separado = frase.split()

print('-'.join(separado))            #Se tenho nomes separados em listas, consigo utilizar o join para juntar uma
                                     #coisa na outra.

                #Para printar um texto muito grande utilize três aspas no inicio e final. 
                #Ex abaixo
'''
#print('''The Zen of Python, by Tim Peters
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!''')
'''
frase = 'Curso em Vídeo Python'

print(frase.upper().count('O'))         #Estou jogando todas as letras para maiúsculas e depois procurando quandos
                                        #'O' maiúsculo eu tenho
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = '   Curso em Vídeo Python   '

print(len(frase.strip()))               #Estou contando quantos caracteres tem na variável frase tirando os espaços 
                                        #inúteis.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

print(frase.lower().find('vídeo'))       #Primeiro coloquei todas as letras da variável em minúsculo e depois procurei
                                         #pela palavra 'vídeo'.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

dividido = frase.split()                 #dividido é uma lista, print(dividido[0]) printa o primeiro item da lista.

print(dividido[0])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frase = 'Curso em Vídeo Python'

dividido = frase.split()
                                         #O dividido[2] é a palavra Vídeo, o [3] é a terceira letra do dividido[2]
print(dividido[2][3])                    #no caso é a letra e.
'''

'''
            DESAFIO 022
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao tdo (sem considerar espaços);
- Quantas letras tem o primeiro nome.

            DESAFIO 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1

            DESAFIO 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo'.

            DESAFIO 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

            DESAFIO 026
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A';
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.

            DESAFIO 027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''