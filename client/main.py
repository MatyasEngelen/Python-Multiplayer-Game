import pygame
from Menu.MainScreen import *

def main():
    pygame.init()
    background_colour = (255,255,255)
    (width, height) = (1280, 720)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("DungeonMybe")
    screen.fill(background_colour)
    pygame.display.flip()

    MainScreen(screen)

if __name__ == "__main__":
    main()