import consts
import pygame


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

    while status:
        user_events_mouse()

main()
