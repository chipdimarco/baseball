# Use the MySportsFeeds API to retrieve MLB info
# 1/27/2018 v3

# IMPORT
import requests
import json
# also import
from lineup import Lineup

# and from my first attempt
# Import the Pygame library
import pygame

from game_settings import Settings
from game_score import Score
import game_functions as gf


'''
# FOR TESTS
# Red Sox ids
# ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
# Yankee ids
#
'''

# Define Colors
BLACK = (   0,   0,   0 )
WHITE = ( 255, 255, 255 )
GREEN = (   0, 255,   0 )
RED   = ( 255,   0,   0 )
BLUE  = (   0,   0, 255 )
GRASS = (   1, 166,  17 )


def main():
    ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
    home = Lineup()
    home_lineup = home.create_lineup_dictionary(ids)
    for i in range ( 0, len(home_lineup)):
        print (home_lineup[i]["lastname"])
        # Initialize the Game Engine
    pygame.init()
    
    # Access Game Settings
    settings = Settings()
    screen = pygame.display.set_mode(settings.size)
    pygame.display.set_caption(settings.caption)
    
    # Access Game Score
    score = Score()

    # Loop until the user is done
    done = False
    
    # Manage screen update rate
    clock = pygame.time.Clock()
    
    # Initialize Scoring
    v_lineup = gf.set_v_lineup()
    h_lineup = gf.set_h_lineup()
    
    # ------- M A I N   P R O G R A M   L O O P ------- #
    while not done:
        gf.check_events(settings, screen)
        
        # --- For each event
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.key == pygame.K_SPACE:
        """     
                
        # --- Game logic here
        
        
        # --- Clear the screen
        screen.fill(GRASS)
        
        # --- Draw everything on the screen
        
        # Draw Field
        gf.draw_field(screen, WHITE)
        gf.draw_scoreboards(screen,BLUE,WHITE,score.v_score,score.h_score)

        # Center Field Scoreboard
        sb_cf_font = pygame.font.SysFont('Calibri', 14, False, True)
        sb_cf_message = sb_cf_font.render("Welcome to Waban Stadium", True, BLACK)
        screen.blit(sb_cf_message,[265, 20])
        
        
        # Lineup card Bottom Left
        if score.half == "top":
            sb_lineup_display = v_lineup
        else:
            sb_lineup_display = h_lineup
            
        pygame.draw.rect(screen, BLACK, [10, 340, 200, 150])
        sb_lineup_font = pygame.font.SysFont('Courier', 12, False, False)
        
        for i in range(len(sb_lineup_display)):
            sb_lineup_message = sb_lineup_font.render(sb_lineup_display[i], True, WHITE)
            screen.blit(sb_lineup_message, [12, 345 + (i*14)])
        
        pygame.display.flip()
        
        # --- 60 frames per second
        clock.tick(60)
    
    # -------      Q U I T   P R O G R A M      ------- #
    pygame.quit()

if __name__ == "__main__":
    main()

