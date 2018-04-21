# Use the MySportsFeeds API to retrieve MLB info
# 3/18/2018: Move Tkinter screen creation to game_screens module
# 3/11/2018: Tkinter mode reads stats from files and layout cleanup
# 2/25/2018: Refactor for console/tkinter modes. Full 9 inning games in either mode
# 2/11/2018 v7: Refactor for putting the game play into the atbat class AND to use Tkinter, not pygame, for interface
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
stadium_name = "Waban Field"

# M A I N   F U N C T I O N
def main():
    # Create Settings object
    settings = Settings()
    # Create Score object
    score = Score()
    # Determine mode
    console_mode = settings.console_mode

    # NOTE: the Tk() class has to be initialized before the Atbat() class because
    # Atbat() needs Tk to define the StringVar() object
    
    #TKINTER MODE
    if not console_mode:
        screen = gs.GameScreen()
        print (f'Initialize Tkinter mode.')
    '''
    #CONSOLE MODE    
    if console_mode:

        # Visitor Setup
        visiting_team_name = "Yankees"

        visitor = Lineup()
        visitor_pitcher_id ="10719"
        visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
        visitor_stats_file = "data/2017_nyy_stats.json"

        visitor.lineup_dictionary = visitor.create_lineup_dictionary_from_file(visitor_stats_file,visitor_ids)
        visitor.lineup_lastname = visitor.create_lineup_lastname(visitor.lineup_dictionary) 
        visitor.pitcher = visitor.get_pitcher_from_file(visitor_stats_file, visitor_pitcher_id)

        # Home Setup
        home_team_name = "Red Sox"

        home = Lineup()
        home_pitcher_id = "10432"
        home_ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
        home_stats_file = "data/2017_bos_stats.json"
            
        home.lineup_dictionary = home.create_lineup_dictionary_from_file(home_stats_file,home_ids)
        home.lineup_lastname = home.create_lineup_lastname(home.lineup_dictionary)
        home.pitcher = home.get_pitcher_from_file(home_stats_file, home_pitcher_id)

        atbat = Atbat()

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
    '''
    # ------- M A I N   P R O G R A M   L O O P ------- #
    if not settings.console_mode:
        screen.mainloop()

if __name__ == "__main__":
    main()
