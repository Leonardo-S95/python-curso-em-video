'''
            DESAFIO 059
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''


valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
sair = 0

while sair != 5:
    opcao = int(input('[ 1 ] SOMAR\n'
                      '[ 2 ] MULTIPLICAR\n'
                      '[ 3 ] QUAL NÚMERO MAIOR\n'
                      '[ 4 ] NOVOS NÚMEROS\n'
                      '[ 5 ] SAIR DO PROGRAMA\n'
                      'Digite a opção desejada: '))
    if opcao == 1:
        print('')
        print('A soma entre {} e {} é igual a {}.'.format(valor1, valor2, valor1 + valor2))
        print('')
    if opcao == 2:
        print('')
        print('A multiplicação entre {} e {} é igual a {}.'.format(valor1, valor2, valor1 * valor2))
        print('')
    if opcao == 3:
        if valor1 > valor2:
            print('')
            print('O número {} é maior que o número {}.'.format(valor1, valor2))
            print('')
        if valor2 > valor1:
            print('')
            print('O número {} é maior que o número {}.'.format(valor2, valor1))
            print('')
        if valor1 == valor2:
            print('')
            print('Os valores digitados são iguais.')
            print('')
    if opcao == 4:
        print('')
        valor1 = int(input('Digite o primeiro valor:'))
        valor2 = int(input('Digite o segundo valor: '))
        print('')
    if opcao == 5:
        sair = 5
    if opcao > 5 or opcao < 1:
        print('\nOpção inválida. Tente novamente.\n')
print('\nPrograma encerrado!')



            #RESPOSTA NO VÍDEO
#from time import sleep
#n1 = int(input('Primeiro valor: '))
#n2 = int(input('Segundo valor: '))
#opção = 0
#while opção != 5:
#    print('''    [ 1 ] somar
#    [ 2 ] multiplicar
#    [ 3 ] maior
#    [ 4 ] novos números
#    [ 5 ] sair do programa''')
#    opção = int(input('Qual é a sua opção? '))
#    if opção == 1:
#        soma = n1 + n2
#        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
#    elif opção == 2:
#        produto = n1 * n2
#       print('O resultado entre {} x {} é {}'.format(n1, n2, produto))
#    elif opção == 3:
#        if n1 > n2:
#            maior = n1
#        else:
#            maior = n2
#        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
#    elif opção == 4:
#        print('Informe os números novamente: ')
#        n1 = int(input('Primeiro valor: '))
#        n2 = int(input('Segundo valor: '))
#    elif opção == 5:
#        print('Finalizando...')
#    else:
#        print('Opção inválida. Tente novamente.')
#    print('=-=' * 10)
#    sleep(2)
#print('Fim do programa! Volte sempre!')
