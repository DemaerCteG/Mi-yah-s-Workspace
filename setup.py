import pygame, sys # imports pygame and sys modules. Graphics, sound, and other features that Pygame provides are in the pygame module
from pygame.locals import * # imports everything from pygame

FPS = 60 # define game FPS
fpsClock = pygame.time.Clock()

pygame.init() # initialize pygame
GAME_WIDTH = 1250
GAME_HEIGHT = 900
GAME_SCREEN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)) # set display window
pygame.display.set_caption('New Game') # set game title


while True: # main game looP

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # player controls go below here...
            
    pygame.display.update()
    fpsClock.tick(FPS)