# takes the batter line and the pitcher line and returns a result
# 2/4/2018 v2
# class Atbat creates the object
# returns a result of hit or out

import random
import sys
from tkinter import *
from tkinter import ttk
from game_settings import Settings


class Atbat():
    def __init__(self):
        self.note = "Atbat"
        self.v_total_runs = 0
        self.h_total_runs = 0
        # StringVar() is a Tkinter() class
        self.play_by_play = StringVar()
        # the .set method puts a string in that object
        self.play_by_play.set("Play by Play goes HERE")

    def play(self, batter, pitcher):
        self.batter = batter
        self.pitcher = pitcher
        # Batter info
        b_last = batter['lastname']
        b_pa = int(batter['plateappearances'])
        b_hits = int(batter['hits'])
        b_bb = int(batter['bb'])
        b_atbats = int(batter['atbats'])
        #
        # Pitcher info
        p_last = pitcher['lastname']
        p_tbf = int(pitcher['totalbattersfaced'])
        p_hits = int(pitcher['hitsallowed'])
        p_bb  = int(pitcher['pitcherwalks'])

        on = b_hits + b_bb + p_hits + p_bb
        total = b_pa + p_tbf
        roll = random.random()
        pct = on/total

        if (roll < pct ):
            return (f'Hit!')
            # Version one with roll feedback
            # return (f'Hit! Roll is {round(roll,3)}; On is {on}; PCT is {round(pct,3)} .')
        else:
            return(f'Out!')
            # Version one with roll feedback
            # return (f'Out!  Roll is {round(roll,3)}; On is {on};  PCT is {round(pct,3)}.')
        
        #return (f'{b_last} is the batter and {p_last} is the pitcher')


    # Top of the inning
    def inning_top (self, inning, visitor_lineup_dictionary, visitor_leads_off_inning, home_pitcher):
        self.inning = inning
        self.visitor_lineup_dictionary=visitor_lineup_dictionary
        self.visitor_leads_off_inning= visitor_leads_off_inning
        self.home_pitcher=home_pitcher
        #self.visitor_up_next =visitor_up_next
        
        out_count = 0
        v_score = 0
        scorecard = (f'Top of Inning {inning}')

        for i in range(9):  
            up = visitor_lineup_dictionary[(i+visitor_leads_off_inning)%9]
            visitor_up_next = (i+visitor_leads_off_inning+1)%9
            r = self.play(up,home_pitcher)

            print (f'{i+1}: {up["lastname"]} - {r}')
            scorecard += (f'\n{i+1}: {up["lastname"]} - {r}')
            if r[0] == "H":
                v_score += 1
            if r[0] == "O":
                out_count += 1
            if out_count > 2:
                break
        visitor_leads_off_inning = visitor_up_next
        self.v_total_runs += v_score
        print ( f'Top of inning {inning} completed.')
        #
        # instead of printing to the console, set the string to the StringVar object.
        #print ( f'{visitor_lineup_dictionary[visitor_leads_off_inning]["lastname"]} will lead off next inning.')
        scorecard += ( f'{visitor_lineup_dictionary[visitor_leads_off_inning]["lastname"]} will lead off next inning.')
        self.play_by_play.set( scorecard)
        result = {}
        result["v_score"]=v_score
        result["visitor_leads_off_inning"]=visitor_leads_off_inning
        return (result)

# BOTTOM of the inning
    def inning_bottom (self, inning, home_lineup_dictionary, home_leads_off_inning, visitor_pitcher):
        self.inning = inning
        self.home_lineup_dictionary=home_lineup_dictionary
        self.home_leads_off_inning= home_leads_off_inning
        self.visitor_pitcher=visitor_pitcher
        
        out_count = 0
        h_score = 0
        scorecard = (f'Bottom of Inning {inning}')

        for i in range(9):  
            up = home_lineup_dictionary[(i+home_leads_off_inning)%9]
            home_up_next = (i+home_leads_off_inning+1)%9
            r = self.play(up,visitor_pitcher)

            print (f'{i+1}: {up["lastname"]} - {r}')
            scorecard += (f'\n{i+1}: {up["lastname"]} - {r}')
            if r[0] == "H":
                h_score += 1
            if r[0] == "O":
                out_count += 1
            if out_count > 2:
                break
        home_leads_off_inning = home_up_next
        self.h_total_runs += h_score
        print ( f'BOTTOM of inning {inning} completed.')
        #
        # instead of printing to the console, set the string to the StringVar object.
        #print ( f'{visitor_lineup_dictionary[visitor_leads_off_inning]["lastname"]} will lead off next inning.')
        scorecard += ( f'{home_lineup_dictionary[home_leads_off_inning]["lastname"]} will lead off next inning.')
        self.play_by_play.set(scorecard)
        result = {}
        result["h_score"]=h_score
        result["home_leads_off_inning"]=home_leads_off_inning
        return (result)


        

'''
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

'''

#example = Atbat()
#print (example.note)
#result = example.play('sale','gardner')
#print (result)
#print (example.play(pitcher='sale',batter='gardner'))