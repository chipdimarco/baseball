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

    def play_out(self, batter, pitcher):
        self.batter = batter
        self.pitcher = pitcher
        # Batter Outs
        b_so = int(batter['batterstrikeouts'])
        b_go = int(batter['battergroundouts'])
        b_ao = int(batter['batterflyouts'])
        # Pitcher Outs
        p_so = int(pitcher['pitcherstrikeouts'])
        p_go = int(pitcher['pitchergroundouts'])
        p_ao = int(pitcher['pitcherflyouts'])
        # Create a Result Array
        result_array = []
        for i in range (b_so + p_so):
            result_array.append('so')
        for j in range (b_go + p_go):
            result_array.append('go')
        for k in range (b_ao + p_ao):
            result_array.append('ao')
        return(random.choice(result_array))


    def play_hit(self,batter,pitcher):
        self.batter = batter
        self.pitcher = pitcher
        # Batter On Base Results
        b_hits = int(batter['hits'])
        b_bb = int(batter['bb'])
        b_2b = int(batter['secondbasehits'])
        b_3b = int(batter['thirdbasehits'])
        b_hr = int(batter['homeruns'])
        b_1b = b_hits - ( b_2b + b_3b + b_hr )
        # Pitcher On Base Results
        p_hits = int(pitcher['hitsallowed'])
        p_bb = int(pitcher['pitcherwalks'])
        p_2b = int(pitcher['secondbasehitsallowed'])
        p_3b = int(pitcher['thirdbasehitsallowed'])
        p_hr = int(pitcher['homerunsallowed'])
        p_1b = p_hits - ( p_2b + p_3b + p_hr )

        # Create the result array
        result_array = []
        for i in range (b_bb + p_bb):
            result_array.append('bb')
        for j in range (b_2b + p_2b):
            result_array.append('2b')
        for k in range (b_3b + p_3b):
            result_array.append('3b')
        for l in range (b_hr + p_hr):
            result_array.append('hr')
        for m in range (b_1b + p_1b):
            result_array.append('1b')
        
        # Result
        return(random.choice(result_array))


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
        r = []

        if (roll < pct ):
            r.append('Hit')
            r.append(self.play_hit(batter,pitcher))
            #return (f'Hit!  type: {hit_type}')
            # Version one with roll feedback
            # return (f'Hit! Roll is {round(roll,3)}; On is {on}; PCT is {round(pct,3)} .')
        else:
            r.append('Out')
            r.append(self.play_out(batter,pitcher))
            #return(f'Out!')
            # Version one with roll feedback
            # return (f'Out!  Roll is {round(roll,3)}; On is {on};  PCT is {round(pct,3)}.')
        return(r)
        #return (f'{b_last} is the batter and {p_last} is the pitcher')


    # Top of the inning
    def inning_top (self, inning, visitor_lineup_dictionary, visitor_leads_off_inning, home_pitcher):
        self.inning = inning
        self.visitor_lineup_dictionary=visitor_lineup_dictionary
        self.visitor_leads_off_inning= visitor_leads_off_inning
        self.home_pitcher=home_pitcher
        
        out_count = 0
        v_score = 0
        scorecard = (f'Top of Inning {inning}')
        print (f'INNING {inning}')
        i = visitor_leads_off_inning

        while out_count < 3:  
            up = visitor_lineup_dictionary[i%9]
            visitor_up_next = (i+1)%9
            r = self.play(up,home_pitcher)

            print (f'  {i+1}: {up["lastname"]} - {r[1]}')
            scorecard += (f'\n{i+1}: {up["lastname"]} - {r[1]}')
            if r[0][0] == "H":
                v_score += 1
            if r[0][0] == "O":
                out_count += 1
            i = visitor_up_next
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
        i = home_leads_off_inning

        while out_count < 3:
            up = home_lineup_dictionary[(i)%9]
            home_up_next = (i+1)%9
            r = self.play(up,visitor_pitcher)

            print (f'  {i+1}: {up["lastname"]} - {r[1]}')
            scorecard += (f'\n{i+1}: {up["lastname"]} - {r[1]}')
            if r[0][0] == "H":
                h_score += 1
            if r[0][0] == "O":
                out_count += 1
            i = home_up_next

        home_leads_off_inning = home_up_next
        self.h_total_runs += h_score
        print ( f'BOTTOM of inning {inning} completed.\n')
        #
        # instead of printing to the console, set the string to the StringVar object.
        #print ( f'{visitor_lineup_dictionary[visitor_leads_off_inning]["lastname"]} will lead off next inning.')
        scorecard += ( f'{home_lineup_dictionary[home_leads_off_inning]["lastname"]} will lead off next inning.')
        self.play_by_play.set(scorecard)
        result = {}
        result["h_score"]=h_score
        result["home_leads_off_inning"]=home_leads_off_inning
        return (result)


    