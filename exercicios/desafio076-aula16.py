'''
            DESAFIO 076
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preçoes, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

catalogo = ('Mouse', 250.00, 'Teclado', 550.00, 'Monitor', 1300.00, 'Cadeira', 500.00, 'Mouse Pad',
            50.00, 'Pen drive', 100.00)

print('=' * 30)
print('LISTA DE PREÇOS'.center(30))
print('=' * 30)

for i in range(0, len(catalogo), 2):
    print(f'{catalogo[i]}.............R${catalogo[i + 1]:.2f}')

print('=' * 30)
