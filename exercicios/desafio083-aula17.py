'''
            DESAFIO 083
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

print('=-' * 30)
print('DESCOBRIDOR DE PARÊNTESES FALTANTES (nice name)'.center(60))
print('=-' * 30)
print()

expressao = list(str(input('Digite a expressão matemática: ')))

if expressao.count('(') == expressao.count(')'):
    print('Os parênteses da expressão tá certin!  (:\n')
else:
    print('Tá faltando parênteses aí, meu chapa!\n')


# Resultado errado caso comece com ). Ex: ) a + b (
