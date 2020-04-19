'''
+ é adição           * é multiplicação      ** é potencia           % é resto da divisão
- é subtração        / é divisão            // é divisão inteira

                   ORDEM DE PRECEDÊNCIA
1º ~> ()
2º ~> **
3º ~> *, /, //, %
4º ~> +, -
'''


n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva outro número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}\nA subtração vale {}\nA multiplicação vale {}\nA divisão vale {:.2f}\nA divisão inteira vale {}\n'
      'O exponencial vale {}'.format(s, sub, m, d, di, e))

'''
                DESAFIO 005
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e 
seu antecessor.
                DESAFIO 006
Crie um algoritmo que leia um número e mostre o seu dobre, tripo e raiz quadrada.
                DESAFIO 007
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a 
sua média.
                DESAFIO 008
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros 
e milímetros.
                DESAFIO 009
Faça um programa que leia um número inteiro qualquer e mostre sua tabuada.
                DESAFIO 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar.
Considere US$1.00 == R$3.27
                DESAFIO 011
Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua 
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de 
tinta pinta uma área de 2m²
                DESAFIO 012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 
5% de desconto.
                DESAFIO 013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo 
salário, com 15% de aumento
'''