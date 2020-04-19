'''
            DESAFIO 043
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

print('\033[34m*\033[m' * 42)
print('\t\t\t\033[1;32mCALCULE SEU IMC\033[m')
print('\033[34m*\033[m' * 42)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura*altura)            #imc = peso / (altura ** 2)  <~ Altura elevada ao quadrado

print('Seu IMC é {:.1f} e se classifica como '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('PESO IDEAL.')
elif 25 <= imc < 30:
    print('SOBREPESO.')
elif 30 <= imc < 40:
    print('OBESIDADE.')
else:                               #elif imc >= 40: para deixar o código explicito.
    print('OBESIDADE MÓRBIDA.')
