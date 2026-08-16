import consts
import pygame
import screen


screen = pygame.display.set_mode((consts.WINDOW_HEIGHT, consts.WINDOW_WIDTH))
screen.fill(consts.BLACK)



# user actions
def user_events_mouse():
    global status
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

status = True


def main():
    pygame.init()

    image = pygame.image.load("soldier.png").convert()
    soldier = pygame.transform.scale(image, (100, 40))
    screen.blit(soldier, (100, 100))
    pygame.display.update()


    while status:
        user_events_mouse()

main()

