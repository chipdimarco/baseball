# 11-02-2019: Add Print and Save box

import sys
import json
from game_settings import Settings

settings = Settings()

def doSomething():
    print ("Do Something")
    return("Did Something")

def done(done):
    return (not done)

#def print_lineup_box (box):
#    for inning in box.linuep:
#        for x in inning:
#            print (x)

def save_box_as_json(box):
    rtext = []
    team = box.team
    for inning in box.lineup:
        for x in inning:
            rtext.append(x)
    box_file = f'{ team }_boxscore.json'
    box = open(box_file, 'w')
    box.write(json.dumps(rtext))
    box.close()
    return( box_file )



