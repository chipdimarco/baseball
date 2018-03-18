# Use the MySportsFeeds API to retrieve MLB info
# 3/11/2018: Tkinter mode reads stats from files and layout cleanup
# 2/25/2018: Refactor for console/tkinter modes. Full 9 inning games in either mode
# 2/16/2018 v8: Get scoreboards and message boards working
# 2/11/2018 v7: Refactor for putting the game play into the atbat class AND to use Tkinter, not pygame, for interface
# 2/4/2018 v5: Use Atbat() to get results and begin creating a loop through a lineup
# 2/3/2018 v4: Add pygame files for functions, score, setting

# IMPORT
from game_lineup import Lineup
from game_atbat import Atbat
from tkinter import *
from tkinter import ttk
from game_settings import Settings
from game_score import Score
import sys

import game_functions as gf
import game_screens as gs

# Variables for sample data
# These need to be configured via the UI
home_team_name = "Red Sox"
visiting_team_name = "Yankees"

home_ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
home_stats_file = "data/2017_bos_stats.json"
'''
visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
visitor_stats_file = "data/2017_nyy_stats.json"
'''
stadium_name = "Waban Field"

# M A I N   F U N C T I O N
def main():
    # Create Settings object
    settings = Settings()

    # Create Lineup objects
    home = Lineup()
    home.lineup_dictionary = home.create_lineup_dictionary_from_file(home_stats_file,home_ids)
    home.lineup_lastname = home.create_lineup_lastname(home.lineup_dictionary)

    '''    
    visitor = Lineup()
    visitor.lineup_dictionary = visitor.create_lineup_dictionary_from_file(visitor_stats_file,visitor_ids)
    visitor.lineup_lastname = visitor.create_lineup_lastname(visitor.lineup_dictionary) 
    '''

    # Create Pitcher Objects
    home_pitcher_id = "10432"
    home.pitcher = home.get_pitcher_from_file(home_stats_file, home_pitcher_id)
    '''
    visitor_pitcher_id ="10719"
    visitor.pitcher = visitor.get_pitcher_from_file(visitor_stats_file, visitor_pitcher_id)
    '''
    # For testing: shows the lineups have been generated properly
    #print (f'{home.pitcher["player"]["LastName"]} is the starting pitcher for the {home_team_name}')
    #print (f'And {visitor.pitcher["player"]["LastName"]} will start for the {visiting_team_name}')
    
    # Create Score object
    score = Score()

    # Determine mode
    console_mode = settings.console_mode

    # NOTE: the Tk() class has to be initialized before the Atbat() class because
    # Atbat() needs Tk to define the StringVar() object
    # Create Screen object
    #screen = Tk()

    screen = gs.GameScreen()

    # Create Atbat object
    atbat = Atbat()

    # Display settings apply in either mode
    v_linescore = []
    h_linescore = []

    #TKINTER MODE
    if not console_mode:
        # Configure screen
        screen.title(settings.caption)
        screen.geometry(settings.size)
        screen.configure(background=settings.screen_background)


        '''
        #BLEACHER BOARD - Frame (0,0) - Top Row
        bleacher_board = ttk.Frame(screen)
        bleacher_board.grid(column=0, row=0)
        bleacher_board.grid_rowconfigure(0,minsize=settings.height/10)
        bleacher_board.grid_columnconfigure(0,minsize=settings.width)
        #ttk.Label(bleacher_board, text = stadium_name, font="Verdana 14 bold").grid(column=0,row =0)
        '''
        '''
        # FIELD BOARD - Frame (0,1) - Middle Row, 3 Columns
        field_board = ttk.Frame(screen)
        field_board.grid(column=0, row =1)
        field_board.grid_columnconfigure(0,minsize=settings.width/4)
        field_board.grid_columnconfigure(1,minsize=settings.width/2)
        field_board.grid_columnconfigure(2,minsize=settings.width/4)
        field_board.grid_rowconfigure(0,minsize=settings.height/2)

        # Field Board > LINEUP CARDS
        viz = (f'VISITORS\n\n{visiting_team_name}\n')
        for i in visitor.lineup_lastname:
            viz += (f'\n{i}')
        hiz = (f'HOME\n\n{home_team_name}\n')
        for i in home.lineup_lastname:
            hiz += (f'\n{i}')

        vlc=StringVar()
        vlc.set(viz)
        v_lineup_card = ttk.Label(field_board, textvariable = vlc)
        v_lineup_card.grid(column= 0, row = 0, sticky=N, padx=12)

        hlc=StringVar()
        hlc.set(hiz)
        h_lineup_card = ttk.Label(field_board, textvariable = hlc)
        h_lineup_card.grid(column= 2, row = 0, sticky=N, padx=12)

        # Field Board > FIELD
        field_height = int(settings.height/2)
        field_width = int(settings.width/2)
        y = int(field_height/4)
        x = int(field_width/4)
        diamond = (2*x,y, 3*x,2*y, 2*x,3*y, x,2*y)
        field = Canvas(field_board,height=field_height,width=field_width)
        field.grid(column=1,row=0)
        field.create_rectangle(0 , 0 , field_width, field_height, fill='#526F35')
        field.create_polygon(diamond, fill=settings.diamond_color)
        
        #DUGOUT - Frame (0,2) - 3 Columns
        dugout = ttk.Frame(screen,padding="3 3 3 12")
        dugout.grid(column=0, row=2)
        dugout.grid_columnconfigure(0,minsize=settings.width/4)
        dugout.grid_columnconfigure(1,minsize=settings.width/4)
        dugout.grid_columnconfigure(2,minsize=settings.width/2)
        dugout.grid_rowconfigure(0,minsize=settings.height*.4)

        # Dugout > PLAY Button
        playNextHalfInningButton = ttk.Button( dugout, text="PLAY", command=lambda: atbat.half_inning(settings, visitor, home))
        playNextHalfInningButton.grid(column=0,row=0, sticky=N, padx=24,pady=24)

        # Dugout > LINESCORE_FRAME        
        linescore_frame = ttk.Frame(dugout)
        linescore_frame.grid(column=1,row=0,sticky=N)

        # Row 0 is Text
        v = StringVar()
        ttk.Label(linescore_frame,textvariable=v).grid(column=1,row=0, sticky = (NW))
        v.set("It's a great day for baseball")
        # Row 1 is Visitors Linescore
        v_linescore = ttk.Label(linescore_frame, textvariable=atbat.v_linescore)
        v_linescore.grid(column=1,row=1,sticky=(NW))
        # Row 2 is Home Linescore
        h_linescore = ttk.Label(linescore_frame, textvariable=atbat.h_linescore)
        h_linescore.grid(column=1,row=2,sticky=(NW))

        # Dugout > PLAY BY PLAY
        # the atbat.inning_top method will also set the play_by_play StringVar, and the message object below will draw it on screen
        message = ttk.Label(dugout,textvariable=atbat.play_by_play)
        message.grid(column=2,row=0,sticky=(NW))
        '''


    #CONSOLE MODE    
    if console_mode:
        for i in range(9):
            # Top of inning
            inning_top = atbat.inning_top(settings.inning + i, visitor.lineup_dictionary, settings.visitor_leads_off_inning, home.pitcher)
            score.v_score += inning_top["v_score"]
            v_linescore.append(inning_top["v_score"])
            settings.visitor_leads_off_inning = inning_top["visitor_leads_off_inning"]
            settings.half_inning = "Bottom"
            print(f'{visiting_team_name}-{score.v_score}')
            print(f'{home_team_name}-{score.h_score}\n')
            # Bottom of inning
            inning_bottom = atbat.inning_bottom(settings.inning + i, home.lineup_dictionary, settings.home_leads_off_inning, visitor.pitcher)
            score.h_score += inning_bottom["h_score"]
            h_linescore.append(inning_bottom["h_score"])
            settings.home_leads_off_inning = inning_bottom["home_leads_off_inning"]
            settings.half_inning="Top"
            print(f'{visiting_team_name}-{score.v_score}')
            print(f'{home_team_name}-{score.h_score}\n')
        
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
    

if __name__ == "__main__":
    main()

