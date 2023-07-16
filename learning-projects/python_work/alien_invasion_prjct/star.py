import pygame
from random import randint
from pygame.sprite import Sprite

class Stars_bg(Sprite):
    '''Class defining star objects in the background of the game'''

    def __init__(self, screen):
        self.screen = screen 
        super(Stars_bg, self).__init__()

        # Choose image and get its rect       
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        
        # Establish its random position on the screen
        self.rect.x = (randint(0, 1440))
        self.rect.y = (randint(0,800))


    