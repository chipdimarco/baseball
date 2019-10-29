# Use the MySportsFeeds API to retrieve MLB info
# 10/20/2019: new version for clibaseball
# 10/26/2019: begin using new functions
# -----------------v1---------------------------
# 3/18/2018: Move Tkinter screen creation to 
#   game_screens module

# IMPORT
from game_lineup import Lineup
from game_atbat import Atbat
from game_settings import Settings
from game_score import Score
import sys

import game_functions as gf
import game_screens as gs
import build_roster as build

# Variables for sample data
stadium_name = "Waban Field"

# M A I N   F U N C T I O N
def main():
    # Create Settings object
    settings = Settings()
    # Create Score object
    score = Score()
    # Determine mode
    console_mode = settings.console_mode

    #CONSOLE MODE    
    if console_mode:
        visiting_team_name = input("Enter Visiting Team: ")
        home_team_name = input("Enter Home Team: ")
        print (f'\nThe matchup: {visiting_team_name} at {home_team_name}\n')
        
        v_linescore = []
        h_linescore = []

        v_lineup_box    = []
        v_pitching_box  = []
        h_lineup_box    = []
        h_pitching_box  = []

        # roster object
        v_roster = build.build_game_roster(visiting_team_name, 2018)
        h_roster = build.build_game_roster(home_team_name, 2018)

        # starters object
        v_starters = build.pick_starters_dh(v_roster)
        h_starters = build.pick_starters_dh(h_roster)
        # returns: rotation, lineup, bullpen, bench

        # batting order object
        v_battingorder = build.make_battingorder(v_starters["lineup"], True)
        h_battingorder = build.make_battingorder(h_starters["lineup"], True)

        # Print Roster info in verbose_mode
        if settings.verbose_mode:
            print(f'\nVisitors\n====')
            print (f'\n{visiting_team_name}\nLineup')
            for x in v_battingorder:
                print (f' {x["Position"]}: {x["LastName"]}')
            print (f'\nRotation')
            for x in v_starters["rotation"]:
                print (f' {x["LastName"]}')
            print (f'\nBullpen')
            for x in v_starters["bullpen"]:
                print (f' {x["LastName"]}')
            print ('\nBench')
            for x in v_starters["bench"]:
                print (f' {x["LastName"]}')
            
            print(f'\nHome\n====')
            print (f'\n{home_team_name}\nLineup')
            for x in h_battingorder:
                print (f' {x["Position"]}: {x["LastName"]}')
            print (f'\nRotation')
            for x in h_starters["rotation"]:
                print (f' {x["LastName"]}')
            print ('\nBullpen')
            for x in h_starters["bullpen"]:
                print (f' {x["LastName"]}')
            print (f'\nBench')
            for x in h_starters["bench"]:
                print (f' {x["LastName"]}')

        visitor = Lineup()
        visitor.pitcher = build.pick_starting_pitcher(v_starters["rotation"])
        visitor.lineup_dictionary = v_battingorder
        visitor.lineup_lastname = visitor.create_lineup_lastname(visitor.lineup_dictionary) 

        home = Lineup()            
        home.pitcher = build.pick_starting_pitcher(h_starters["rotation"])
        home.lineup_dictionary = h_battingorder
        home.lineup_lastname = home.create_lineup_lastname(home.lineup_dictionary)

        print (f'Pitching Matchup')
        print (f'{visiting_team_name}         {home_team_name}')
        print (f'{visitor.pitcher["FirstName"]} {visitor.pitcher["LastName"]}  {home.pitcher["FirstName"]} {home.pitcher["LastName"]}')
        atbat = Atbat()

        for i in range(9):
            # Top of inning
            inning_top = atbat.inning_top(settings.inning + i, visitor.lineup_dictionary, settings.visitor_leads_off_inning, home.pitcher)
            score.v_score += inning_top["v_score"]
            v_linescore.append(inning_top["v_score"])
            settings.visitor_leads_off_inning = inning_top["visitor_leads_off_inning"]
            settings.half_inning = "Bottom"
            v_lineup_box.append(inning_top["lineup_box"])
            h_pitching_box.append(inning_top["pitching_box"])
            print(f'{visiting_team_name}-{score.v_score}')
            print(f'{home_team_name}-{score.h_score}\n')
            # Bottom of inning
            inning_bottom = atbat.inning_bottom(settings.inning + i, home.lineup_dictionary, settings.home_leads_off_inning, visitor.pitcher)
            score.h_score += inning_bottom["h_score"]
            h_linescore.append(inning_bottom["h_score"])
            settings.home_leads_off_inning = inning_bottom["home_leads_off_inning"]
            settings.half_inning="Top"
            h_lineup_box.append(inning_bottom["lineup_box"])
            v_pitching_box.append(inning_bottom["pitching_box"])
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

        print (f"\n\n--------------- v lineup box -----")
        gf.print_lineup_box(v_lineup_box)

    # ------- M A I N   P R O G R A M   L O O P ------- #

if __name__ == "__main__":
    main()
