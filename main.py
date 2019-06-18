
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


# ---------------------------------------- HELPERS

def draw_stick_figure(screen, x, y):
    # head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)


# ---------------------------------------- MAIN

done = False

while not done:
    # process events
    for event in pygame.event.get():

    	# user presses the X button
        if event.type == pygame.QUIT:
            done = True
            break

        # user pressed an arrow key on keyboard
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # user releases key
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
	
	# draw background color
    screen.fill(WHITE)

    # move person
    x_coord += x_speed
    y_coord += y_speed

    # draw
    draw_stick_figure(screen, x_coord, y_coord)
 
    # update the screen with what we've drawn.
    pygame.display.flip()
 
    # frames per second
    CLOCK.tick(60)
 
# quit the game
pygame.quit()

# hi this is a test 
