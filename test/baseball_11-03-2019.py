# -----------------v2---------------------------
# Use the MySportsFeeds API to retrieve MLB info
# 10/20/2019: new version for clibaseball
# 11/02/2019: Box class
# -----------------v1---------------------------
# 3/18/2018: Move Tkinter screen creation to game_screens module

# IMPORT
import sys

from game_lineup import Lineup
from game_atbat import Atbat
from game_settings import Settings
from game_score import Score
from game_box import Box

import game_functions as gf
import game_screens as gs
import build_roster as build

#   V A R I A B L E S
stadium_name = "Waban Field"
PLAY_BY_PLAY = False
YEAR         = 2018

#   M A I N   F U N C T I O N
def main():
    #   Create Settings object
    settings = Settings()
    #   Create Score object
    score = Score()
    #   Determine mode
    console_mode = settings.console_mode

    #  CONSOLE MODE    
    if console_mode:
        # INPUT
        visiting_team_name = input("Enter Visiting Team: ")
        home_team_name     = input("Enter Home Team: ")
        if PLAY_BY_PLAY:
            print (f'\nThe matchup: {visiting_team_name} at {home_team_name}\n')

        #   Create Box Score Objects        
        v_box   = Box( visiting_team_name )
        h_box   = Box( home_team_name )

        #   Create Roster Objects
        v_roster = build.build_game_roster( visiting_team_name, YEAR )
        h_roster = build.build_game_roster( home_team_name, YEAR )

        #   Create Starters Objects
        #   returns lists: rotation, lineup, bullpen, bench
        v_starters = build.pick_starters_dh(v_roster)
        h_starters = build.pick_starters_dh(h_roster)

        #   Create Batting Order Object
        v_battingorder = build.make_battingorder(v_starters["lineup"], True)
        h_battingorder = build.make_battingorder(h_starters["lineup"], True)

        #   Print Roster Info when using verbose_mode
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

        #   Create Lineup Objects
        visitor = Lineup()
        visitor.pitcher = build.pick_starting_pitcher(v_starters["rotation"])
        visitor.lineup_dictionary = v_battingorder
        visitor.lineup_lastname = visitor.create_lineup_lastname(visitor.lineup_dictionary) 

        home = Lineup()            
        home.pitcher = build.pick_starting_pitcher(h_starters["rotation"])
        home.lineup_dictionary = h_battingorder
        home.lineup_lastname = home.create_lineup_lastname(home.lineup_dictionary)

        print (f'Pitching Matchup')
        print ( visiting_team_name.ljust(18," ") + home_team_name )
        print (f'{ visitor.pitcher["FirstName"] } { visitor.pitcher["LastName"] }'.ljust(17," ") + f' { home.pitcher["FirstName"]} {home.pitcher["LastName"]}')
        
        atbat = Atbat()

        for i in range(9):
            # TOP OF INNING
            inning_top = atbat.inning_top(settings.inning + i, visitor.lineup_dictionary, settings.visitor_leads_off_inning, home.pitcher)
            score.v_score += inning_top["v_score"]
            v_box.linescore.append(inning_top["v_score"])
            settings.visitor_leads_off_inning = inning_top["visitor_leads_off_inning"]
            settings.half_inning = "Bottom"
            v_box.lineup.append(inning_top["lineup_box"])
            h_box.pitching.append(inning_top["pitching_box"])
            if PLAY_BY_PLAY:
                print(f'{visiting_team_name}-{score.v_score}')
                print(f'{home_team_name}-{score.h_score}\n')
            #   BOTTOM OF INNING
            inning_bottom = atbat.inning_bottom(settings.inning + i, home.lineup_dictionary, settings.home_leads_off_inning, visitor.pitcher)
            score.h_score += inning_bottom["h_score"]
            h_box.linescore.append(inning_bottom["h_score"])
            settings.home_leads_off_inning = inning_bottom["home_leads_off_inning"]
            settings.half_inning="Top"
            h_box.lineup.append(inning_bottom["lineup_box"])
            v_box.pitching.append(inning_bottom["pitching_box"])
            if PLAY_BY_PLAY:
                print(f'{visiting_team_name}-{score.v_score}')
                print(f'{home_team_name}-{score.h_score}\n')
        
        #   P O S T G A M E
        print (f'\nGAME OVER')
        print (visiting_team_name, end='   ')
        for r in v_box.linescore:
            print (r, end = ' ')
        print (f' -- {score.v_score}')

        print (home_team_name, end='   ')
        for r in h_box.linescore:
            print (r, end = ' ')
        print (f' -- {score.h_score}')

        v_box_file = v_box.save_box_as_json (v_box)
        h_box_file = h_box.save_box_as_json (h_box)
        print (v_box.print_box( v_box_file ))
        print (h_box.print_box( h_box_file ))


    # ------- M A I N   P R O G R A M   L O O P ------- #

if __name__ == "__main__":
    main()
