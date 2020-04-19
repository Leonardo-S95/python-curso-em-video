'''
            DESAFIO 056
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''


somaidade = 0
media = 0
idadevelho = 0
nomevelho = ''
cont = 0

for i in range(0, 4):
    nome = str(input('Qual o {}º nome? '.format(i + 1))).title().strip()
    idade = int(input('Qual a idade do(a) {}? '.format(nome)))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade
    print('')
    if i == 0 and sexo == 'M':              #sexo in 'Mm' funciona para caso digite m maiúsculo ou minúsculo.
        nomevelho = nome
        idadevelho = idade
    if sexo in 'Mm' and idade > idadevelho:         #Coloquei sexo in 'Mm' só pra diferenciar.
        nomevelho = nome
        idadevelho = idade
    if sexo == 'F' and idade < 20:
        cont += 1

media = somaidade / 4

print('A média de idade do grupo é de {:.2f} anos.'.format(media))
print('O homem mais velho é o {} com {} anos.'.format(nomevelho, idadevelho))
print('Nessa lista, {} mulher(es) têm menos de 20 anos.'.format(cont))



'''
            #RESPOSTA NO VÍDEO

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

'''