# 10-28-2019
# box score class
# 11-2-2019: Add print_box method

import json
import os

class Box():
    def __init__(self, team):
        # team name
        self.team = team
        # list of players with keys ID AB H R BB
        self.lineup = []
        # list of pitchers with keys ID IP H K W R
        self.pitching = []
        # list of runs scored in an inning
        self.linescore = []

    def save_box_as_json(self, box):
        rtext = []
        team = box.team
        for inning in box.lineup:
            for x in inning:
                rtext.append(x)
        box_file = f'results/{ team }_boxscore.json'
        box = open(box_file, 'w')
        box.write(json.dumps(rtext))
        box.close()
        return( box_file )


    def print_box ( self, box_file ):
        print ()
        handler = open( box_file ,'r')
        data = handler.read()
        stats=json.loads(data)
        boxlines = []
        processedids = []
        for i in stats:
            if i["ID"] in processedids:
                pass
            else:
                id = i["ID"]
                boxline = {}
                boxline["BO"] = i["BO"]
                boxline["NAME"] = i["NAME"] + " - " + i["POS"]
                boxline["ID"] = id
                boxline["AB"] = 0
                boxline["H"]  = 0
                boxline["BB"] = 0
                boxline["HR"] = 0
                for j in stats:
                    if j["ID"] == id:
                        boxline["AB"] += j["AB"]
                        boxline["H"]  += j["H"]
                        boxline["BB"] += j["BB"]
                        boxline["HR"] += j["HR"]
                processedids.append(id)
                boxlines.append(boxline)
        handler.close()

        boxtotal = {}
        boxtotal["NAME"] = "TOTAL - - - - - -"
        boxtotal["AB"] = 0
        boxtotal["H"]  = 0
        boxtotal["BB"] = 0
        boxtotal["HR"] = 0
        for k in stats:
            boxtotal["AB"] += k["AB"]
            boxtotal["H"]  += k["H"]
            boxtotal["BB"] += k["BB"]
            boxtotal["HR"] += k["HR"]
        boxlines.append(boxtotal)

        print(self.team.ljust(20," ") + "AB   H  BB  HR")
        for x in boxlines:
            N  = x["NAME"].ljust(18,' ')
            AB = str(x["AB"]).rjust(4,' ')
            H  = str(x["H"]).rjust(4,' ')
            BB = str(x["BB"]).rjust(4, ' ')
            HR = str(x["HR"]).rjust(4, ' ')
            print (N + AB + H + BB + HR)
