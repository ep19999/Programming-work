import sys


import pygame
from pygame.sprite import Group
from time import sleep

from settings import Settings, Background
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initialise pygame, settings and screen object
    pygame.init()
    clock = pygame.time.Clock()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Start Game (Press Enter)")

    # Create instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the background, a ship, a group of bullets and a group of aliens.
    background = Background([0,0])
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(background, ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()


