
# ---------------------------------------- IMPORTS

import pygame
from player import Player

# ---------------------------------------- CONSTANTS & GLOBALS

# some colors in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# dimensions of the screen
WIDTH  = 700 # pixels
HEIGHT = 500 # pixels

# title of the game
GAME_TITLE = 'Our Pacman Game'

# clock to determine refresh rate
CLOCK = pygame.time.Clock()


# ---------------------------------------- PRE-GAME SETUP

# init the game
pygame.init()

# make game screen dimensions according to setup
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# set game caption to specifed value
pygame.display.set_caption(GAME_TITLE)

# hide the mouse cursor
pygame.mouse.set_visible(0)

# speed in pixels per frame
x_speed = 0
y_speed = 0
 
# current position
x_coord = 10
y_coord = 10


# ---------------------------------------- MAIN

done = False

while not done:
    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
	
	# draw background color
    screen.fill(WHITE)
 
    # update the screen with what we've drawn.
    pygame.display.flip()
 
    # frames per second
    CLOCK.tick(60)
 
# quit the game
pygame.quit()
