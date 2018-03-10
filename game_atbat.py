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
        self.play_by_play.set("- - - Play by Play - - - ")
        # StringVar() for linescore
        self.v_linescore = StringVar()
        self.v_linescore.set("Visitor: ")
        self.h_linescore = StringVar()
        self.h_linescore.set("Home: ")

    def play_out(self, batter, pitcher):
        self.batter = batter
        self.pitcher = pitcher
        # Batter Outs
        b_so = int(batter['stats']['BatterStrikeouts']['#text'])
        b_go = int(batter['stats']['BatterGroundOuts']['#text'])
        b_ao = int(batter['stats']['BatterFlyOuts']['#text'])
        # Pitcher Outs
        p_so = int(pitcher['stats']['PitcherStrikeouts']['#text'])
        p_go = int(pitcher['stats']['PitcherGroundOuts']['#text'])
        p_ao = int(pitcher['stats']['PitcherFlyOuts']['#text'])
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
        b_hits = int(batter['stats']['Hits']['#text'])
        b_bb = int(batter['stats']['BatterWalks']['#text'])
        b_2b = int(batter['stats']['SecondBaseHits']['#text'])
        b_3b = int(batter['stats']['ThirdBaseHits']['#text'])
        b_hr = int(batter['stats']['Homeruns']['#text'])
        b_1b = b_hits - ( b_2b + b_3b + b_hr )
        # Pitcher On Base Results
        p_hits = int(pitcher['stats']['HitsAllowed']['#text'])
        p_bb = int(pitcher['stats']['PitcherWalks']['#text'])
        p_2b = int(pitcher['stats']['SecondBaseHitsAllowed']['#text'])
        p_3b = int(pitcher['stats']['ThirdBaseHitsAllowed']['#text'])
        p_hr = int(pitcher['stats']['HomerunsAllowed']['#text'])
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
        b_last = batter['player']['LastName']
        #print(batter['stats']['PlateAppearances'])
        b_pa = int(batter['stats']['PlateAppearances']['#text'])
        b_hits = int(batter['stats']['Hits']['#text'])
        b_bb = int(batter['stats']['BatterWalks']['#text'])
        b_atbats = int(batter['stats']['AtBats']['#text'])
        #
        # Pitcher info
        p_last = pitcher['player']['LastName']
        p_tbf = int(pitcher['stats']['TotalBattersFaced']['#text'])
        p_hits = int(pitcher['stats']['HitsAllowed']['#text'])
        p_bb  = int(pitcher['stats']['PitcherWalks']['#text'])

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

    def run_the_bases(self,scenario,ac):
        self.scenario = scenario
        self.ac = ac
        bases_empty =  (0,0,0)
        bases_loaded = (1,1,1)
        on_first =     (0,0,1)
        on_second =    (0,1,0)
        on_third =     (1,0,0)
        first_second = (0,1,1)
        first_third =  (1,0,1)
        second_third = (1,1,0)
        if scenario == bases_empty:
            if ac in ['bb','1b']:
                return([on_first,0])
            elif ac == '2b':
                return([on_second,0])
            elif ac == '3b':
                return([on_third,0])
            elif ac == 'hr':
                return([bases_empty,1])
            else:
                return(scenario,0)
        if scenario == on_first:
            if ac in ['bb','1b']:
                return([first_second,0])
            elif ac == '2b':
                return([second_third,0])
            elif ac == '3b':
                return([on_third,1])
            elif ac == 'hr':
                return([bases_empty,2])
            else:
                return(scenario,0)
        if scenario == on_second:
            if ac == 'bb':
                return([first_second,0])
            elif ac == '1b':
                return([first_third,0])
            elif ac == '2b':
                return([on_second,1])
            elif ac == '3b':
                return([on_third,1])
            elif ac == 'hr':
                return([bases_empty,2])
            else:
                return(scenario,0)
        if scenario == on_third:
            if ac == 'bb':
                return([first_third,0])
            elif ac == '1b':
                return([on_first,1])
            elif ac == '2b':
                return([on_second,1])
            elif ac == '3b':
                return([on_third,1])
            elif ac == 'hr':
                return([bases_empty,2])
            else:
                return(scenario,0)
        if scenario == first_second:
            if ac == 'bb':
                return([bases_loaded,0])
            elif ac == '1b':
                return([bases_loaded,0])
            elif ac == '2b':
                return([second_third,1])
            elif ac == '3b':
                return([on_third,2])
            elif ac == 'hr':
                return([bases_empty,3])
            else:
                return(scenario,0)
        if scenario == first_third:
            if ac == 'bb':
                return([bases_loaded,0])
            elif ac == '1b':
                return([first_second,1])
            elif ac == '2b':
                return([second_third,1])
            elif ac == '3b':
                return([on_third,2])
            elif ac == 'hr':
                return([bases_empty,3])
            else:
                return(scenario,0)
        if scenario == second_third:
            if ac == 'bb':
                return([bases_loaded,0])
            elif ac == '1b':
                return([first_third,1])
            elif ac == '2b':
                return([on_second,2])
            elif ac == '3b':
                return([on_third,2])
            elif ac == 'hr':
                return([bases_empty,3])
            else:
                return(scenario,0)
        if scenario == bases_loaded:
            if ac == 'bb':
                return([bases_loaded,1])
            elif ac == '1b':
                return([bases_loaded,1])
            elif ac == '2b':
                return([second_third,2])
            elif ac == '3b':
                return([on_third,3])
            elif ac == 'hr':
                return([bases_empty,4])
            else:
                return(scenario,0)

    def half_inning(self, settings, visitor, home):
        if settings.done:
            print ("Game Over")
            return("Game Over")
        inning = settings.inning
        half_inning = settings.half_inning
        if inning < 9:
            pass
        elif inning == 9:
            if self.h_total_runs > self.v_total_runs:
                if half_inning == "Bottom":
                    settings.done = True
                    result = (f'Game Over')
                    print(result)
                    return(result)
        else:
            if self.h_total_runs != self.v_total_runs:
                if half_inning == "Top":
                    settings.done = True
                    result = (f'Game Over')
                    print (result)
                    return(result)
        result = (f'{half_inning} of inning {inning}')
        print (result)
        
        if ( half_inning == "Top"):
            result = self.inning_top(settings.inning, visitor.lineup_dictionary, settings.visitor_leads_off_inning, home.pitcher)
            settings.half_inning = "Bottom"
            self.v_linescore.set(f'{self.v_linescore.get()} {str(result["v_score"])}')
            settings.visitor_leads_off_inning = result["visitor_leads_off_inning"]
            
        else:
            result = self.inning_bottom(settings.inning, home.lineup_dictionary, settings.home_leads_off_inning, visitor.pitcher)
            settings.half_inning = "Top"
            self.h_linescore.set(f'{self.h_linescore.get()} {str(result["h_score"])}')
            settings.inning += 1
            settings.home_leads_off_inning = result["home_leads_off_inning"]
        return (settings,visitor,home)

    # TOP of the inning
    def inning_top (self, inning, visitor_lineup_dictionary, visitor_leads_off_inning, home_pitcher):
        self.inning = inning
        self.visitor_lineup_dictionary=visitor_lineup_dictionary
        self.visitor_leads_off_inning= visitor_leads_off_inning
        self.home_pitcher=home_pitcher
        
        out_count = 0
        scenario = (0,0,0)
        runthebases=[scenario,0]
        v_score = 0
        scorecard = (f'Top of Inning {inning}')
        print (f'INNING {inning}')
        i = visitor_leads_off_inning

        while out_count < 3:  
            up = visitor_lineup_dictionary[i%9]
            visitor_up_next = (i+1)%9
            r = self.play(up,home_pitcher)

            #print (f'  {i+1}: {up["lastname"]} - {r[1]}')
            scorecard += (f'\n{i+1}: {up["player"]["LastName"]} - {r[1]}')
            if r[0][0] == "H":
                # scenario 0-7 and advance_code comes from play result
                runthebases = self.run_the_bases(scenario,r[1])
                scenario = runthebases[0]
                v_score += runthebases[1]
                #v_score += 1
            if r[0][0] == "O":
                out_count += 1
                runthebases[1]=0
            print (f'  {i+1}: {up["player"]["LastName"]} - {r[1]} - runs scored: {runthebases[1]} runners: {scenario}')
            i = visitor_up_next
        visitor_leads_off_inning = visitor_up_next
        self.v_total_runs += v_score
        print ( f'Top of inning {inning} completed.')
        #
        # instead of printing to the console, set the string to the StringVar object.
        #print ( f'{visitor_lineup_dictionary[visitor_leads_off_inning]["lastname"]} will lead off next inning.')
        scorecard += ( f'\n{visitor_lineup_dictionary[visitor_leads_off_inning]["player"]["LastName"]} will lead off next inning.')
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
        scenario = (0,0,0)
        runthebases=[scenario,0]
        h_score = 0
        scorecard = (f'Bottom of Inning {inning}')
        i = home_leads_off_inning

        while out_count < 3:
            up = home_lineup_dictionary[(i)%9]
            home_up_next = (i+1)%9
            r = self.play(up,visitor_pitcher)

            #print (f'  {i+1}: {up["lastname"]} - {r[1]}')
            scorecard += (f'\n{i+1}: {up["player"]["LastName"]} - {r[1]}')
            if r[0][0] == "H":
                runthebases = self.run_the_bases(scenario,r[1])
                scenario = runthebases[0]
                h_score += runthebases[1]
                #h_score += 1
            if r[0][0] == "O":
                out_count += 1
                runthebases[1]=0
            print (f'  {i+1}: {up["player"]["LastName"]} - {r[1]} -   runs scored: {runthebases[1]}   runners: {scenario}')
            i = home_up_next

        home_leads_off_inning = home_up_next
        self.h_total_runs += h_score
        print ( f'BOTTOM of inning {inning} completed.\n')
        #
        # instead of printing to the console, set the string to the StringVar object.
        #print ( f'{visitor_lineup_dictionary[visitor_leads_off_inning]["lastname"]} will lead off next inning.')
        scorecard += ( f'\n{home_lineup_dictionary[home_leads_off_inning]["player"]["LastName"]} will lead off next inning.')
        self.play_by_play.set(scorecard)
        result = {}
        result["h_score"]=h_score
        result["home_leads_off_inning"]=home_leads_off_inning
        return (result)






    