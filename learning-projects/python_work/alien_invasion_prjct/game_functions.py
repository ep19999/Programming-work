import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from star import Stars_bg
from settings import Background
from ship import Ship 

def check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets):
    '''Respond to keydown events'''
    if  event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif  event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif  event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_RETURN:
        print("starting game")
        start_game(ai_settings, screen, stats, ship, aliens, bullets)

        
def fire_bullet(ai_settings, screen, ship, bullets):
    '''Fire a bullet if limit not reached yet.'''
    # Create new bullet add to bullet group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''Respond to keyup events'''
    if  event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif  event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_q:
        sys.exit()
    #if  event.key == pygame.K_DOWN:
    #    ship.moving_down = False
    #if  event.key == pygame.K_UP:
    #    ship.moving_up = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    '''Respond to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:                
            check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start new game when player presses play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)
        

def start_game(ai_settings, screen, stats, ship, aliens, bullets):
    """Start new game when play button activated"""
    # Hide mouse cursor.
    pygame.mouse.set_visible(False)
    # Reset game statistics.
    stats.reset_stats()
    stats.game_active = True

    # Reset the game settings
    ai_settings.initialize_dynamic_settings()

    # Empty list of aliens and bullets.
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the ship.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(background, ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # Redraw screen during each pass
    screen.fill(ai_settings.bg_colour)
    screen.blit(background.image, background.rect)
    # Redraw bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
           
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''Update position of bullets and get rid of old bullets.'''
    bullets.update()

    #Remove bullets off screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Check for collisions.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Destroy exisitng bullets, speed up game and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def create_stars(ai_settings, screen, stars):
    '''Create group of stars for the game background'''
    
    star_num = ai_settings.num_stars
    
    for i in range(star_num):
        print(i)
        star = Stars_bg(screen)
        stars.add(star)
        

def get_number_aliens_x(ai_settings, alien_width):
    '''Determine the number of aliens that fit in a row'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (1.3 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    '''Determine the number of rows of aliens that fit on the screen.'''
    available_space_y = (ai_settings.screen_height - (6 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''Create an alien and place it in the row.'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width / 2 + 1.3 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2.5 * alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens):
    '''Create a full fleet of aliens.'''
    # Create alien and find number of aliens in row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Create fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    '''Respond if aliens reach an edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''Drop entire fleet and change the fleet's direction.'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    # Decrement ships_left.
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        ship.moving_right = 0

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reach the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat same as if ship was hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''Update positions of aliens in the fleet'''
    check_fleet_edges(ai_settings, aliens)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)





