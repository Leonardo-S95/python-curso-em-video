'''
                DESAFIO 021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''


from pygame import mixer
mixer.init()
mixer.music.load('D021.mp3')
mixer.music.play()
input('Tá ouvindo?')


#O input acima é para deixar o programa rodando. Caso o delete a música não toca.
#
#        ESSE CÓDIGO ABRE O PLAYER DE MÚSICA DO COMPUTADOR
#import os
#os.startfile(r'C:\Users\Leonardo\Documents\Music\Matanza - A arte do insulto.mp3')
