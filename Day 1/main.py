import pygame, sys # imports pygame and sys modules. Graphics, sound, and other features that Pygame provides are in the pygame module
from pygame.locals import * # imports everything from pygame

FPS = 60 # define game FPS
fpsClock = pygame.time.Clock()

pygame.init() # initialize pygame
GAME_WIDTH = 1250
GAME_HEIGHT = 900
GAME_SCREEN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)) # set display window
pygame.display.set_caption('New Game') # set game title

RED = (255, 0, 0) # max is 255
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Block:
    def __init__(self, x, y, width, height, color):
        self.direction = 'right'
        self.speed = 20
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(GAME_SCREEN, self.color, self.rect) # x, y, width, height

    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x == 1000:
                self.direction = 'down'
        
        if self.direction == "down":
            self.rect.y += self.speed
            if self.rect.y == 700:
                self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x == 400:
                self.direction = 'up'

        if self.direction == 'up':
            self.rect.y -= self.speed
            if self.rect.y == 100:
                self.direction = 'right'


block = Block(400, 100, 90, 100, WHITE)

while True: # main game looP
    GAME_SCREEN.fill(BLACK)
    # this is where all the code for our game will be
    # everything below is constantly repeating

    block.draw()
    block.move()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # player controls go below here...
            
    pygame.display.update()
    fpsClock.tick(FPS)