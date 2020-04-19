'''
            DESAFIO 062
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostras 0 termos.
'''

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = 1
maistermos = 0

print('Os 10 primeiros termos da PA com o primeiro termo sendo {} e a razão {} são: '.format(n, r))

while t <= 10:
    if t == 1:
        print(n)
        t += 1
    else:
        n += r
        print(n)
        t += 1

print('')
maistermos = str(input('Deseja ver mais 10 termos? [S/N]')).strip().upper()
print('')

while maistermos == 'S':
    t = 1
    while t <= 10:
        if t == 1:
            n += r
            print(n)
            t += 1
        else:
            n += r
            print(n)
            t += 1
    print('')
    maistermos = str(input('Deseja ver mais 10 termos? [S/N]')).strip().upper()
    print('')

print('\033[1mPrograma encerrado!\033[m')



'''
            #RESPOSTA NO VÍDEO
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

'''
