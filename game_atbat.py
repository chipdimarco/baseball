# takes the batter line and the pitcher line and returns a result
# 2/4/2018 v1
# 10/27/2019 v2
# class Atbat creates the object
# returns a result of hit or out

import random
import sys
from game_settings import Settings


class Atbat():
    def __init__(self):
        self.note = "Atbat"
        self.v_total_runs = 0
        self.h_total_runs = 0
        self.v_box = {}
        self.h_box = {}
        self.play_by_play = False

    def play_out(self, batter, pitcher):
        self.batter = batter
        self.pitcher = pitcher
        b_so = batter['SO']
        b_go = batter['GO']
        b_ao = batter['FO']
        # Pitcher Outs
        p_so = pitcher['K']
        p_go = pitcher['PGO']
        p_ao = pitcher['PFO']
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
        b_hits = batter['H']
        b_bb   = batter['BB']
        b_1b   = batter['1B']
        b_2b   = batter['2B']
        b_3b   = batter['3B']
        b_hr   = batter['HR']
        # Pitcher On Base Results
        p_hits = pitcher['HA']
        p_bb   = pitcher['BBA']
        p_1b   = pitcher['1BA']
        p_2b   = pitcher['2BA']
        p_3b   = pitcher['3BA']
        p_hr   = pitcher['HRA']

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
        b_bo = batter['bo']
        b_id = batter['ID']
        b_name = batter['LastName']
        b_pa = batter['PA']
        b_hits = batter['1B']+batter['2B']+batter['3B']+batter['HR']
        b_bb = batter['BB']
        #
        # Pitcher info
        p_id   = pitcher['ID']
        p_name = pitcher['LastName']
        p_tbf  = pitcher['TBF']
        p_hits = pitcher['1BA']+pitcher['2BA']+pitcher['3BA']+pitcher['HRA']
        p_bb   = pitcher['BBA']
        #
        on    = b_hits + b_bb + p_hits + p_bb
        total = b_pa + p_tbf
        roll  = random.random()
        pct   = on/total
        r     = {}
        # TALLY BATTER STATS HERE
        lineup_box = {}
        lineup_box["BO"]   = b_bo
        lineup_box["ID"]   = b_id
        lineup_box["NAME"] = b_name
        lineup_box["POS"]  = batter["Position"]
        lineup_box["AB"]   = 0
        lineup_box["H"]    = 0
        lineup_box["BB"]   = 0
        lineup_box["HR"]   = 0
        # TALLY PITCHER STATS HERE
        pitching_box = {}
        pitching_box["ID"] = p_id
        pitching_box["NAME"] = p_name
        pitching_box["BF"] = 0
        pitching_box["HA"] = 0
        pitching_box["K"]  = 0
        pitching_box["W"]  = 0
        pitching_box["O"]  = 0
        #
        if (roll < pct ):
            r["result"] = "Hit"
            box = self.play_hit(batter, pitcher)
            if box == 'bb':
                lineup_box["BB"] = 1
                pitching_box["W"] = 1
            else:
                lineup_box["AB"] = 1
                lineup_box["H"]  = 1
                pitching_box["HA"] = 1
            if box == 'hr':
                lineup_box["HR"] = 1
        else:
            r["result"] = 'Out'
            box = self.play_out(batter,pitcher)
            lineup_box["AB"]  = 1
            pitching_box["O"] = 1
            if box == "so":
                pitching_box["K"] = 1
        r["description"]  = box
        r["lineup_box"]   = lineup_box
        r["pitching_box"] = pitching_box
        return(r)

    def test_gameover(self,h,v,half,inning):
        result = {
            "done": False,
            "h": h,
            "v": v,
            "half": half,
            "inning": inning,
            "check": False
        }
        if inning < 9:
            result["check"] = True
        elif half == "T":
            result["check"] = True
        elif h == v:
            result["check"] = True
        elif h > v:
            result["check"] = True
            result["done"] = True
        elif h != v and half == "F":
            result["check"] = True
            result["done"] = True
        return(result)

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

    #   Returns settings, visitor, home, result
    #   Calls inning_top and inning_bottom
    def half_inning(self, settings, visitor, home):
        if settings.done:
            print ("Game Over")
            return("Game Over")
        inning = settings.inning
        half_inning = settings.half_inning
        result = (f'{half_inning} of inning {inning}')
        if self.play_by_play:
            print (result)
        
        if ( half_inning == "Top"):
            check_score = self.test_gameover( self.h_total_runs, self.v_total_runs, half_inning, inning)
            if check_score['done'] == True:
                settings.done = True
                result = (f'Game Over')
                print (result)
                return ( settings, visitor, home, result )
            result = self.inning_top(settings.inning, visitor.lineup_dictionary, settings.visitor_leads_off_inning, home.pitcher)
            settings.half_inning = "Bottom"
#            self.v_linescore.set(f'{self.v_linescore.get()} {str(result["v_score"])}')
            v_linescore.set(f'{self.v_linescore.get()} {str(result["v_score"])}')
            settings.visitor_leads_off_inning = result["visitor_leads_off_inning"]
            
        else:
            check_score = self.test_gameover( self.h_total_runs, self.v_total_runs, half_inning, inning)
            if check_score['done'] == True:
                settings.done = True
                result = (f'Game Over')
                print (result)
                return ( settings, visitor, home, result )
            result = self.inning_bottom(settings.inning, home.lineup_dictionary, settings.home_leads_off_inning, visitor.pitcher)
            settings.half_inning = "Top"
            self.h_linescore.set(f'{self.h_linescore.get()} {str(result["h_score"])}')
            settings.inning += 1
            settings.home_leads_off_inning = result["home_leads_off_inning"]
        return ( settings, visitor, home, result )

    # TOP of the inning
    def inning_top (self, inning, visitor_lineup_dictionary, visitor_leads_off_inning, home_pitcher):
        self.inning = inning
        self.visitor_lineup_dictionary=visitor_lineup_dictionary
        self.visitor_leads_off_inning= visitor_leads_off_inning
        self.home_pitcher=home_pitcher
        #
        out_count = 0
        scenario = (0,0,0)
        runthebases=[scenario,0]
        v_score = 0
        scorecard = (f'Top of Inning {inning}')
        if self.play_by_play:
            print (f'INNING {inning}')
        i = visitor_leads_off_inning
        lineup_box   = []
        pitching_box = []
        #
        while out_count < 3:
            up = visitor_lineup_dictionary[i%9]
            visitor_up_next = (i+1)%9
            r = self.play(up,home_pitcher)
            scorecard += (f'\n{i+1}: {up["LastName"]} - {r["description"]}')
            if r["result"][0] == "H":
                # scenario 0-7 and advance_code comes from play result
                runthebases = self.run_the_bases(scenario,r["description"])
                scenario = runthebases[0]
                v_score += runthebases[1]
            if r["result"][0] == "O":
                out_count += 1
                runthebases[1]=0
            if self.play_by_play:
                print (f'  {i+1}: {up["LastName"]} - {r["description"]} - runs scored: {runthebases[1]} runners: {scenario}')
            lineup_box.append(r["lineup_box"])
            pitching_box.append(r["pitching_box"])
            i = visitor_up_next
        visitor_leads_off_inning = visitor_up_next
        self.v_total_runs += v_score
        if self.play_by_play:
            print ( f'Top of inning {inning} completed.')
        #
        scorecard += ( f'\n{visitor_lineup_dictionary[visitor_leads_off_inning]["LastName"]} will lead off next inning.')
        result = {}
        result["v_score"]=v_score
        result["visitor_leads_off_inning"]=visitor_leads_off_inning
        result["lineup_box"]   = lineup_box
        result["pitching_box"] = pitching_box
        return (result)

    # BOTTOM of the inning
    def inning_bottom (self, inning, home_lineup_dictionary, home_leads_off_inning, visitor_pitcher):
        #self.inning = inning
        self.home_lineup_dictionary=home_lineup_dictionary
        self.home_leads_off_inning= home_leads_off_inning
        self.visitor_pitcher=visitor_pitcher
        #        
        out_count = 0
        scenario = (0,0,0)
        runthebases=[scenario,0]
        h_score = 0
        scorecard = (f'Bottom of Inning {inning}')
        lineup_box   = []
        pitching_box = []
        i = home_leads_off_inning
        #
        while out_count < 3:
            up = home_lineup_dictionary[(i)%9]
            home_up_next = (i+1)%9
            r = self.play(up,visitor_pitcher)
            scorecard += (f'\n{i+1}: {up["LastName"]} - {r["description"]}')
            if r["result"][0] == "H":
                # scenario 0-7 and advance_code comes from play result
                runthebases = self.run_the_bases(scenario,r["description"])
                scenario = runthebases[0]
                h_score += runthebases[1]
            if r["result"][0] == "O":
                out_count += 1
                runthebases[1]=0
            if self.play_by_play:
                print (f'  {i+1}: {up["LastName"]} - {r["description"]} - runs scored: {runthebases[1]} runners: {scenario}')
            lineup_box.append(r["lineup_box"])
            pitching_box.append(r["pitching_box"])
            i = home_up_next

        home_leads_off_inning = home_up_next
        self.h_total_runs += h_score
        if self.play_by_play:
            print ( f'BOTTOM of inning {inning} completed.\n')
        #
        scorecard += ( f'\n{home_lineup_dictionary[home_leads_off_inning]["LastName"]} will lead off next inning.')
        result = {}
        result["h_score"]=h_score
        result["home_leads_off_inning"]=home_leads_off_inning
        result["lineup_box"]   = lineup_box
        result["pitching_box"] = pitching_box

        return (result)






    