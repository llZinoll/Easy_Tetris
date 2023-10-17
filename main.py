import pygame,sys
from function import *
from blocks import *

pygame.init()
red = (255, 0, 0)

#with this we define the width and height of the screen
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python tetris")

clock = pygame.time.Clock()

game_grid = Grid()

block = TBlock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    #Drawing
    screen.fill(red)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)
