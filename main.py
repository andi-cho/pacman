
# ---------------------------------------- IMPORTS

import pygame
from player import Player

# ---------------------------------------- CONSTANTS & GLOBALS

# dimensions of the screen
WIDTH  = 700 # pixels
HEIGHT = 500 # pixels

# title of the game
GAME_TITLE = 'Our Pacman Game'

clock = None


# ---------------------------------------- PRE-GAME SETUP

# init the game
pygame.init()

# make game screen dimensions according to setup
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# set game caption to specifed value
pygame.display.set_caption(GAME_TITLE)


# ---------------------------------------- MAIN

pygame.quit()
