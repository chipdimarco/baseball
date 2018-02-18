# Use the MySportsFeeds API to retrieve MLB info
# 2/16/2018 v8: Get scoreboards and message boards working
# 2/11/2018 v7: Refactor for putting the game play into the atbat class AND to use Tkinter, not pygame, for interface
# 2/4/2018 v5: Use Atbat() to get results and begin creating a loop through a lineup
# 2/3/2018 v4: Add pygame files for functions, score, setting

# IMPORT
#import requests
#import json
# also import
from game_lineup import Lineup
from game_atbat import Atbat
from tkinter import *
from tkinter import ttk
from game_settings import Settings
from game_score import Score
import sys

import game_functions as gf

# Variables for sample data
home_team_name = "Red Sox"
visiting_team_name = "Yankees"
home_ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
stadium_name = "Waban Field"

# Game functions
def main():
    # Create Lineups
    home = Lineup()
    home_lineup_dictionary = home.create_lineup_dictionary(home_ids)
    home_lineup_lastname = home.lineup_lastname(home_lineup_dictionary)
    # Confirm
    print (home_lineup_lastname)
    
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
    #print (f'{home_pitcher["lastname"]} allowed {home_pitcher["homerunsallowed"]} homeruns last year.')
    
    # Access Game Score
    score = Score()

    # Access Game Settings
    # NOTE: the Tk() class has to be initialized before the Atbat() class because
    # Atbat() needs Tk to define the StringVar() object
    settings = Settings()
    console_mode = settings.console_mode
    screen = Tk()
    atbat = Atbat()

    #TKINTER MODE
    if not console_mode:    
        screen.title(settings.caption)
        screen.geometry(settings.size)
        #BLEACHER BOARD - Frame (0,0)
        bleacher_board = ttk.Frame(screen)
        bleacher_board.grid(column=0, row=0)
        ttk.Label(bleacher_board, text = stadium_name).grid(column=0,row =0)
        # FIELD BOARD FRAME (0,1)
        field_board = ttk.Frame(screen)
        field_board.grid(column=0, row =1)
        # LINEUP CARDS
        viz = (f'VISITORS\n{visiting_team_name}')
        for i in visitor_lineup_lastname:
            viz += (f'\n{i}')

        vlc=StringVar()
        vlc.set(viz)
        v_lineup_card = ttk.Label(field_board, textvariable = vlc)
        v_lineup_card.grid(column= 0, row = 0, sticky=N)

        hlc=StringVar()
        hlc.set(f'HOME\n{home_team_name}')
        h_lineup_card = ttk.Label(field_board, textvariable = hlc)
        h_lineup_card.grid(column= 2, row = 0, sticky=N)

        field_height = int(settings.height/2)
        field_width = int(settings.width/2)
        y = int(field_height/4)
        x = int(field_width/4)
        diamond = (2*x,y, 3*x,2*y, 2*x,3*y, x,2*y)
        field = Canvas(field_board,height=field_height,width=field_width)
        field.grid(column=1,row=0)
        field.create_rectangle(0 , 0 , field_width, field_height, fill='green')
        field.create_polygon(diamond, fill=settings.diamond_color)

        dugout = ttk.Frame(screen,padding="3 3 3 12")
        dugout.grid(column=0, row=2)

        v = StringVar()
        ttk.Label(dugout,textvariable=v).grid(column=0,row=0, sticky = W)
        v.set("It's a great day for baseball")
    
        playButton = ttk.Button(screen, text="Play", command=lambda: atbat.inning_top(settings.inning, visitor_lineup_dictionary, settings.visitor_leads_off_inning, home_pitcher))
        playButton.grid(column=0,row=3, sticky=W)
        # the atbat.inning_top method will also set the play_by_play StringVar, and the message object below will draw it on screen
        message = ttk.Label(dugout,textvariable=atbat.play_by_play)
        message.grid(column=0,row=1)


    #CONSOLE MODE    
    if console_mode:
        v_linescore = []
        h_linescore = []
        for i in range(9):
            # Top of inning
            inning_top = atbat.inning_top(settings.inning + i, visitor_lineup_dictionary, settings.visitor_leads_off_inning, home_pitcher)
            score.v_score += inning_top["v_score"]
            v_linescore.append(inning_top["v_score"])
            settings.visitor_leads_off_inning = inning_top["visitor_leads_off_inning"]
            settings.half_inning = "Bottom"
            # Bottom of inning
            inning_bottom = atbat.inning_bottom(settings.inning + i, home_lineup_dictionary, settings.home_leads_off_inning, visitor_pitcher)
            score.h_score += inning_bottom["h_score"]
            h_linescore.append(inning_bottom["h_score"])
            settings.home_leads_off_inning = inning_bottom["home_leads_off_inning"]
            settings.half_inning="Top"
        #print (f'Visitors Total: {score.v_score}')
        print (f'\nGAME OVER')
        print (visiting_team_name, end='   ')
        for r in v_linescore:
            print (r, end = ' ')
        print (f' -- {score.v_score}')

        print (home_team_name, end='   ')
        for r in h_linescore:
            print (r, end = ' ')
        print (f' -- {score.h_score}')
    




    
    # ------- M A I N   P R O G R A M   L O O P ------- #
    if not settings.console_mode:
        screen.mainloop()
    '''
    while not done:
        screen.mainloop()
    '''



if __name__ == "__main__":
    main()

