'''
            DESAFIO 085
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
pares e ímpares em ordem crescente.

# Primeira tentativa

num = []
par = []
impar = []

for i in range(0, 7):
    num.append(int(input(f'Digite o {i + 1}º número: ')))

    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        impar.append(num[i])

num.clear()
num.append(par[:])          # Foi meio q uma trapaça pra obedecer o enunciado
num.append(impar[:])
par.sort()
impar.sort()

print()
print(f'Os valores pares são: {par}\nOs valores ímpares são: {impar}')
'''

# Segunda tentativa pegando somente esse num = [[], []] do vídeo resposta, já que não foi ensinado

num = [[], []]
temp = 0

for i in range(0, 7):
    temp = int(input(f'Digite o {i + 1}º número: '))
    if temp % 2 == 0:
        num[0].append(temp)
    else:
        num[1].append(temp)

num[0].sort()
num[1].sort()
print(f'\nNúmeros pares digitados ~> {num[0]}\n'
      f'Números ímpares digitados ~> {num[1]}')
