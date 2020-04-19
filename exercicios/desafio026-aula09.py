'''
            DESAFIO 026
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A';
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma linda frase aqui: ')).lower().strip()

print('A quantidade de letra A dessa frase é: ', frase.count('a'))

print('A posição do primeiro A é na casa de número: {}'.format(frase.find('a')+1))     #Tendo Arara como exemplo, a
                                                                                       #posição do primeiro A é 0.
print('A posição do último A é na casa de número: {}'.format(frase.rfind('a')+1))      #Esse +1 serve para mostrar
                                                                                       #ao usuário do programa uma
                                                                                       #contagem que começa do 1.

'''
            #RESPOSTA NO VÍDEO
            
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
'''