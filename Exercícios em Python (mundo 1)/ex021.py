import pygame

pygame.init()   
pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")
# "audio.mp3" é exemplo de nome do arquivo que será executado.
pygame.mixer.music.play()
input()
pygame.event.wait()