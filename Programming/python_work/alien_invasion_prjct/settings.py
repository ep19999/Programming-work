import pygame

class Settings():
    '''Class to store ai settings'''

    def __init__(self):
        '''Initialize game's static settings'''
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_colour = (255, 255, 255)
    
        #Ship settings
        self.ship_limit = 2

        #Bullet settings
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = 110, 248, 154
        self.bullets_allowed = 10
        # self.firing_speed = 1

        #Background objects settings
        self.num_stars = 25
        self.star_colour = (255, 255, 255)

        #Alien settings
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        "Initialize settings that change throughout the game"
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 1

        # fleet_direction
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

class Background():
    '''Class to customise the games background'''

    def __init__(self, location):
        self.image = pygame.image.load('images/bg5.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


