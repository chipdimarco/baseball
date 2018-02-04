# takes the batter line and the pitcher line and returns a result
# 2/3/2018 v1
# class Atbat creates the object
# returns the result of the plate appearance

import random

class Atbat():
    def __init__(self):
        self.note = "Atbat"

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
            return (f'Hit! Roll is {round(roll,3)}; On is {on}; PCT is {round(pct,3)} .')
        else:
            return (f'Out!  Roll is {round(roll,3)}; On is {on};  PCT is {round(pct,3)}.')
        
        #return (f'{b_last} is the batter and {p_last} is the pitcher')

#example = Atbat()
#print (example.note)
#result = example.play('sale','gardner')
#print (result)
#print (example.play(pitcher='sale',batter='gardner'))