import pygame
import screen

def soldier():
    image = pygame.image.load("soldier.png").convert_alpha()
    soldier = pygame.transform.scale(image, (100, 40))
    screen.blit(soldier, (0, 0))
    pygame.display.update()

def place_soldier():