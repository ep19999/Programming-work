import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''Initialize ship and set starting position'''
        self.screen = screen
        self.ai_settings = ai_settings

        #Load ship image and get its rect
        self.image = pygame.image.load('learning-projects/python_work/alien_invasion_prjct/images/human_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at bottom centre.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal value for ship center.
        self.position = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False
        
   
    def update(self):
        '''Update ship's position based on the movement flag.'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.position +=  self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.position -=  self.ai_settings.ship_speed_factor
        # if self.moving_up and self.rect.top > self.screen_rect.top:
        #     self.rect.centery -= self.ai_settings.ship_speed_factor
        # if self.moving_down and self.rect.bottom < 800:
        #     self.rect.centery += self.ai_settings.ship_speed_factor

        
        self.rect.centerx = self.position

    def blitme(self):
        '''Draw the ship at current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.position = self.screen_rect.centerx
        
        