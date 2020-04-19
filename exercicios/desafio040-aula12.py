'''
            DESAFIO 040
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('A média é {:.1f}.\nO aluno foi \033[31mREPROVADO!\033[m'.format(media))

elif media >= 5 and media < 7:
    print('A média é {:.1f}.\nO aluno está de \033[33mRECUPERAÇÃO!\033[m'.format(media))

else:
    print('A média é {:.1f}.\nO aluno está \033[34mAPROVADO!\033[m'.format(media))


'''
            #RESPOSTA NO VÍDEO
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))
if 7 > média >=5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
'''
