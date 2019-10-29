# 10-28-2019
# box score class

class Box():
    def __init__(self):
        # team name
        self.team = "TEAMNAME"
        # list of players with keys ID AB H R BB
        self.lineup = []
        # list of pitchers with keys ID IP H K W R
        self.pitching = []
        # list of runs scored in an inning
        self.linescore = []