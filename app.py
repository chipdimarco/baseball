# Use the MySportsFeeds API to retrieve MLB info
# 2/4/2018 v5: Use Atbat() to get results and begin creating a loop through a lineup
# 2/3/2018 v4: Add pygame files for functions, score, setting

# IMPORT
import requests
import json
# also import
from game_lineup import Lineup
from game_atbat import Atbat

# and from my first attempt
# Import the Pygame library
# import pygame
from tkinter import *
from tkinter import ttk

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
    # Setup game_functions will occur here
    # Select a Home Team
    # Red Soxs are Home Team
    home_team_name = "Red Sox"
    # Select a Visiting Team
    # Yankees are Visiting Team
    visiting_team_name = "Yankees"
    # Create a roster for each team
    # Select the lineup. There will be a string of ids for each lineup.
    home_ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
    visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
   
    # Create Lineups
    home = Lineup()
    home_lineup_dictionary = home.create_lineup_dictionary(home_ids)
    home_lineup_lastname = home.lineup_lastname(home_lineup_dictionary)
    
    # Confirm
    # print (home_lineup_lastname)
    visitor = Lineup()
    visitor_lineup_dictionary = visitor.create_lineup_dictionary(visitor_ids)
    visitor_lineup_lastname = visitor.lineup_lastname(visitor_lineup_dictionary) 
    # Confirm
    #print (visitor_lineup_lastname)
     #
    # And Select a pitcher for each team
    home_pitcher_id = ['10432']
    home_pitcher = home.get_pitcher(home_pitcher_id)

    visitor_pitcher_id =['10719']
    visitor_pitcher = visitor.get_pitcher(visitor_pitcher_id)

    print (f'{home_pitcher["lastname"]} is the starting pitcher for the {home_team_name}')
    print (f'And {visitor_pitcher["lastname"]} will start for the {visiting_team_name}')

    print (f'{home_pitcher["lastname"]} allowed {home_pitcher["homerunsallowed"]} homeruns last year.')
    
    # Access Game Score
    score = Score()
    # score.v_score = 0
    # score.h_score = 0



    #v6 Loop 9 times
    atbat = Atbat()
    visitor_leads_off_inning = 0
    home_leads_off_inning = 0
    out_count = 0
    
    for inning in range(9):
        # Top of the inning
        out_count = 0
        for i in range(9):
            up = visitor_lineup_dictionary[(i+visitor_leads_off_inning)%9]
            visitor_up_next = (i+visitor_leads_off_inning+1)%9
            r = atbat.play(up,home_pitcher)
            print (f'{i+1}: {up["lastname"]} - {r}')
            if r[0] == "H":
                score.v_score += 1
            if r[0] == "O":
                out_count += 1
            if out_count > 2:
                break
        visitor_leads_off_inning = visitor_up_next
        print ( f'Top of inning {inning+1} completed.')
        print ( f'{visitor_lineup_dictionary[visitor_leads_off_inning]["lastname"]} will lead off next inning.') 
        print()
        # Bottom of the inning
        out_count = 0
        for i in range(9):
            up = home_lineup_dictionary[(i+home_leads_off_inning)%9]
            home_up_next = (i+home_leads_off_inning+1)%9
            r = atbat.play(up,visitor_pitcher)
            print (f'{i+1}: {up["lastname"]} - {r}')
            if r[0] == "H":
                score.h_score += 1
            if r[0] == "O":
                out_count += 1
            if out_count > 2:
                break
        home_leads_off_inning = home_up_next
        print ( f'Bottom of inning {inning+1} completed.')
        print ( f'{home_lineup_dictionary[home_leads_off_inning]["lastname"]} will lead off next inning.') 
        print ()
    print (f'Game Over')
    print (f'Visitor Hits: {score.v_score}  Home Hits: {score.h_score}')


    # Initialize the Game Engine
    # pygame.init()
    
    # Access Game Settings
    settings = Settings()
    #screen = pygame.display.set_mode(settings.size)
    #pygame.display.set_caption(settings.caption)
    screen = Tk()
    screen.title(settings.caption)

    #this should be a method in Settings, yes?
    mainframe = ttk.Frame(screen, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N,W,S,E))
    mainframe.columnconfigure(0,weight=1)
    mainframe.rowconfigure(0,weight=1)

    ttk.Label(mainframe,text="VISITOR").grid(column=2,row=2,sticky=W)
    ttk.Label(mainframe,text="Welcome to Home Field").grid(column=3,row=2)
    ttk.Label(mainframe,text="HOME").grid(column=4, row =2, sticky=E)
    
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5,pady=5)

    screen.mainloop()


    # Loop until the user is done
    done = True
    #done = False
    
    '''
    # Manage screen update rate
    clock = pygame.time.Clock()
    '''

    # Initialize Scoring
    
    
    # ------- M A I N   P R O G R A M   L O O P ------- #
    while not done:
        # gf.check_events(settings, screen)
        
        # --- For each event
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.key == pygame.K_SPACE:
        """     
                
        # --- Game logic here
        
        '''
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
            sb_lineup_display = visitor_lineup_lastname
        else:
            sb_lineup_display = home_lineup_lastname
            
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
    '''

if __name__ == "__main__":
    main()

