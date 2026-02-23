import pygame

pygame.mixer.init()
pygame.mixer.music.load('mendiga.mp3')
pygame.mixer.music.play()
input('Aperte Enter para encerrar...')