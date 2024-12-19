import pygame
pygame.init()   
pygame.mixer.init()
pygame.mixer.music.load("lgbt.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()