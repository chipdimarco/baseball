# -----------------v2---------------------------
# 11/3/2019 refactor as class
# - 11/23/2019 add score display and extra innings handler
# - 11/25/2019 substitute pitchers

# IMPORT
import sys
import random
import math

from game_lineup import Lineup
from game_atbat import Atbat
from game_settings import Settings
from game_score import Score
from game_box import Box

import game_functions as gf
import game_screens as gs
import build_roster as build
import db

#   V A R I A B L E S
stadium_name = "Waban Field"
SAVE_STATS   = True
PLAY_BY_PLAY = True
YEAR         = 2019

#   M A I N   F U N C T I O N
class Game():
    def __init__(self):
    #   Create Settings object
        self.settings = Settings()
    #   Create Score object
        self.score = Score()
    #   Set Game Number 
        self.game_number = 0

    def get_game_input(self):
        # INPUT
        self.visiting_team_name = input("Enter Visiting Team: ")
        self.home_team_name     = input("Enter Home Team: ")
        return("Teams set")

    def set_scheduled_game_input(self, v, h):
        self.visiting_team_name = v
        self.home_team_name     = h

    def get_game_objects(self):
        #   Create Box Score Objects        
        self.v_box   = Box( self.visiting_team_name )
        self.h_box   = Box( self.home_team_name )
        #   Create Roster Objects
        self.v_roster = build.build_game_roster( self.visiting_team_name, YEAR )
        self.h_roster = build.build_game_roster( self.home_team_name, YEAR )
        #   Create Starters Objects
        #   returns lists: rotation, lineup, bullpen, bench
        self.v_starters = build.pick_starters_dh( self.v_roster )
        self.h_starters = build.pick_starters_dh( self.h_roster )
        #   Create Batting Order Object
        self.v_battingorder = build.make_battingorder( self.v_starters["lineup"], True )
        self.h_battingorder = build.make_battingorder( self.h_starters["lineup"], True )
        #   Create Lineup Objects
        #   Visitor Lineup Object
        self.visitor = Lineup()
        self.visitor.pitcher = build.pick_starting_pitcher( self.v_starters["rotation"] )
        self.visitor.starting_pitcher_id = self.visitor.pitcher["ID"]
        self.visitor.lineup_dictionary = self.v_battingorder
        self.visitor.lineup_lastname = self.visitor.create_lineup_lastname( self.visitor.lineup_dictionary ) 
        #   Home Lineup Object
        self.home = Lineup()            
        self.home.pitcher           = build.pick_starting_pitcher( self.h_starters["rotation"] )
        self.home.starting_pitcher_id = self.home.pitcher["ID"]
        self.home.lineup_dictionary = self.h_battingorder
        self.home.lineup_lastname   = self.home.create_lineup_lastname( self.home.lineup_dictionary )
        #
        if PLAY_BY_PLAY:
            print (f'\nPitching Matchup')
            print ( self.visiting_team_name.ljust(18," ") + self.home_team_name )
            print (f'{ self.visitor.pitcher["FirstName"] } { self.visitor.pitcher["LastName"] }'.ljust(17," ") + f' { self.home.pitcher["FirstName"]} {self.home.pitcher["LastName"]}')
            print (f'--------------------------------')
        return("Objects set")


        #   Print Roster Info when using verbose_mode
    def print_roster_info(self):
        print(f'\nVisitors\n====')
        print (f'\n{ self.visiting_team_name }\nLineup')
        for x in self.v_battingorder:
            print (f' { x["Position"] }: { x["LastName"]}' )
        print (f'\nRotation')
        for x in self.v_starters["rotation"]:
            print (f' {x["LastName"]}')
        print (f'\nBullpen')
        for x in self.v_starters["bullpen"]:
            print (f' {x["LastName"]}')
        print ('\nBench')
        for x in self.v_starters["bench"]:
            print (f' {x["LastName"]}')
        
        print(f'\nHome\n====')
        print (f'\n{ self.home_team_name }\nLineup')
        for x in self.h_battingorder:
            print (f' {x["Position"]}: {x["LastName"]}')
        print (f'\nRotation')
        for x in self.h_starters["rotation"]:
            print (f' {x["LastName"]}')
        print ('\nBullpen')
        for x in self.h_starters["bullpen"]:
            print (f' {x["LastName"]}')
        print (f'\nBench')
        for x in self.h_starters["bench"]:
            print (f' {x["LastName"]}')

        print (f'Pitching Matchup')
        print ( self.visiting_team_name.ljust(18," ") + self.home_team_name )
        print (f'{ self.visitor.pitcher["FirstName"] } { self.visitor.pitcher["LastName"] }'.ljust(17," ") + f' { self.home.pitcher["FirstName"]} {self.home.pitcher["LastName"]}')

    def final_score_display(self, check_score):
        if check_score["h"] > check_score["v"]:
            print (f'{ self.visiting_team_name } { check_score["v"] } - { self.home_team_name } { check_score["h"] }' + f'{ " in " + str(check_score["inning"]) if check_score["inning"] > 9 else ""}')
        elif check_score["v"] > check_score["h"]:
            print (f'{ self.home_team_name } { check_score["h"] } - { self.visiting_team_name } { check_score["v"] }' + f'{ " in " + str(check_score["inning"]) if check_score["inning"] > 9 else ""}') 
        else:
            print (f'TIE in {check_score["inning"]}: { self.home_team_name } { check_score["h"] } - { self.visiting_team_name } { check_score["v"] } ') 

    def check_substitutions_top(self,i):
        p = self.home.pitcher
        print (f'Top {i}th', end=": ")
        if p["ID"] == self.home.starting_pitcher_id:
            if math.floor((i/9)*100) < random.randrange(100):
                print (f'{self.home.pitcher["LastName"]} stays in.')
                return()
        ps    = []
        ps.append(p)
        p_ids = []
        p_ids.append(p["ID"])
        for x in self.h_box.pitching:
            for y in x:
                if y["ID"] in p_ids:
                    pass
                else:
                    p_ids.append(y["ID"])
        if len(self.h_starters["bullpen"]) > 0:
            rp = random.choice(self.h_starters["bullpen"])
            print (f'New Pitcher: { rp["FirstName"] } { rp["LastName"]}')
            self.h_starters["bullpen"].remove(rp)
            self.home.pitcher = rp

    def check_substitutions_bottom(self,i):
        p = self.visitor.pitcher
        print (f'Bottom {i}th', end=": ")
        if p["ID"] == self.visitor.starting_pitcher_id:
            if math.floor((i/9)*100) < random.randrange(100):
                print (f'{self.visitor.pitcher["LastName"]} stays in.')
                return()
        ps    = []
        ps.append(p)
        p_ids = []
        p_ids.append(p["ID"])
        for x in self.v_box.pitching:
            for y in x:
                if y["ID"] in p_ids:
                    pass
                else:
                    p_ids.append(y["ID"])
        if len(self.v_starters["bullpen"]) > 0:
            rp = random.choice(self.v_starters["bullpen"])
            print (f'New Pitcher: { rp["FirstName"] } { rp["LastName"]}')
            self.v_starters["bullpen"].remove(rp)
            self.visitor.pitcher = rp

    def play_game(self):
        self.atbat = Atbat()
        # Loop through innings
        i = 1
        while i < 30:
            # TOP OF INNING
            check_score = self.atbat.test_gameover(self.score.h_score,self.score.v_score, "T", i)
            if check_score['done'] == True:
                self.settings.done = True
                self.final_score_display(check_score)
                return (  )
            # check_substitutions - change the pitcher for 7th
            if i >= 7:
                self.check_substitutions_top(i)
            inning_top = self.atbat.inning_top( self.settings.inning + i, self.visitor.lineup_dictionary, self.settings.visitor_leads_off_inning, self.home.pitcher)
            self.score.v_score += inning_top["v_score"]
            self.v_box.linescore.append( inning_top["v_score"])
            self.settings.visitor_leads_off_inning = inning_top["visitor_leads_off_inning"]
            self.settings.half_inning = "Bottom"
            self.v_box.lineup.append( inning_top["lineup_box"])
            self.h_box.pitching.append( inning_top["pitching_box"])
            #   BOTTOM OF INNING
            check_score = self.atbat.test_gameover(self.score.h_score,self.score.v_score, "B", i)
            # check_substitutions - change the pitcher for 7th
            if i >= 7:
                self.check_substitutions_bottom(i)
            if check_score['done'] == True:
                self.settings.done = True
                self.final_score_display(check_score)
                return (  )
            inning_bottom = self.atbat.inning_bottom( self.settings.inning + i, self.home.lineup_dictionary, self.settings.home_leads_off_inning, self.visitor.pitcher )
            self.score.h_score += inning_bottom["h_score"]
            self.h_box.linescore.append(inning_bottom["h_score"])
            self.settings.home_leads_off_inning = inning_bottom["home_leads_off_inning"]
            self.settings.half_inning="Top"
            self.h_box.lineup.append(inning_bottom["lineup_box"])
            self.v_box.pitching.append(inning_bottom["pitching_box"])
            #   Check score again at the end of the bottom of the inning
            check_score = self.atbat.test_gameover(self.score.h_score,self.score.v_score, "F", i)
            if check_score['done'] == True:
                self.settings.done = True
                self.final_score_display(check_score)
                return (  )
            i += 1
        


    #   P O S T G A M E
    def postgame(self):
        if PLAY_BY_PLAY:
            print (f'\nGAME OVER')
            print ( self.visiting_team_name, end='   ')
            for r in self.v_box.linescore:
                print (r, end = ' ')
            print (f' -- { self.score.v_score }')

            print ( self.home_team_name, end='   ')
            for r in self.h_box.linescore:
                print (r, end = ' ')
            print (f' -- { self.score.h_score }')

        v_box_file = self.v_box.save_box_as_json ( self.v_box )
        h_box_file = self.h_box.save_box_as_json ( self.h_box )

        if SAVE_STATS:
            stats =  db.save_box_to_db(self.v_box, self.game_number)
            if stats:
                print ("Stats ran")
            else:
                print ("Stats failed")

        if PLAY_BY_PLAY:
            print ( self.v_box.print_box( v_box_file ))
            print ( self.h_box.print_box( h_box_file ))
        
        #for p in self.v_box["pitching"]
        
        return ( self.visiting_team_name, self.score.v_score, self.home_team_name, self.score.h_score)


