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
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.speed = 10
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(GAME_SCREEN, self.color, self.rect) # x, y, width, height

    def move(self):
        if self.left == True and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.right == True and self.rect.right < 1250:
            self.rect.x += self.speed
        if self.up == True and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.down == True and self.rect.bottom < 900:
            self.rect.y += self.speed

block = Block(400, 100, 90, 100, WHITE)

while True: # main game loop
    GAME_SCREEN.fill(BLACK)
    
    block.draw()
    block.move()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # player controls go below here...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                block.left = True
            if event.key == pygame.K_d:
                block.right = True
            if event.key == pygame.K_w:
                block.up = True
            if event.key == pygame.K_s:
                block.down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                block.left = False
            if event.key == pygame.K_d:
                block.right = False
            if event.key == pygame.K_w:
                block.up = False 
            if event.key == pygame.K_s:
                block.down = False  

            
    pygame.display.update()
    fpsClock.tick(FPS)