                #Primeiro código(style) é o estilo(negrito, itálico..),
                #segundo código(text) é da cor do texto, terceiro código(back) é da cor do fundo.
                #Códigos Style que funcionam melhor no Python -> 0(none), 1(Bold), 4(Underline, 7(Negative)
                #Códigos Text -> 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(magenta),
                #                36(ciano), 37(cinza)
                #Código Back -> 40(branco) até 47(cinza), as cores estão na mesma ordem que as de cima.


print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[30;42mTeste')
print('\033[mTeste')        #Padrão do terminal(fundo preto, letra cinza).
print('\033[7;30mTeste')    #Negativo inverteu a cor da letra com a cor do fundo e vice versa.

print('\033[1;32;46mOlá, Mundo!\033[m')
print('\033[7;32;46mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\33[m e \033[31m{}\033[m!!'.format(a, b))

nome = 'Leonardo'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))


'''
            DESAFIO
Colocar cores nos desafios anteriores.
'''