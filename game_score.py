#import pygame
#pygame.init()

class Score():
    def __init__(self):
        self.inning = 1
        self.half = "top"
        self.v_score = 0
        self.h_score = 0
        
    def process_box (self):
        return ("demo")
        handler = open( 'boxscore.json','r')
        data = handler.read()
        #data = handler.readlines()
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
                boxline["NAME"] = i["NAME"]
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

        print("                 AB   H  BB  HR")
        for x in boxlines:
            N  = x["NAME"].ljust(15,' ')
            AB = str(x["AB"]).rjust(4,' ')
            H  = str(x["H"]).rjust(4,' ')
            BB = str(x["BB"]).rjust(4, ' ')
            HR = str(x["HR"]).rjust(4, ' ')
            print (N + AB + H + BB + HR)
