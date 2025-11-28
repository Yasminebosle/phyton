import pygame
import random 
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

SCREEN-WIDTH,SCREEN_HEIGHT=500,400

MOVEMENT_SPEED=5

FONT_SIZE=72

background_image=pygame.transform.scale(pygame.image.load('download.jpeg'))