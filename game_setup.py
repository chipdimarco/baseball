# 3/20/2018

import tkinter as tk
from tkinter import ttk
import json

screen = tk.Tk()
screen.title("Testing")
screen_width=900
screen_height=600
screen.geometry(f'{screen_width}x{screen_height}')
screen.configure(background="gray")


# Choose Teams
# From game_screens, from Setup
# select_VisitingTeam
# select_HomeTeam
# Team Selection
team_codes = {
    'Red Sox':'bos',
    'Yankees':'nyy',
    'Cubs':'chc',
    'Rays':'tb',
    'Astros':'hou',
    'Phillies':'phi'
}
options_Teams = ["Red Sox","Yankees", "Astros", "Rays", "Cubs", "Phillies"]
select_VisitingTeam = tk.StringVar(screen)
visitingteamoptions = options_Teams
select_HomeTeam = tk.StringVar(screen)
hometeamoptions = options_Teams
select_VisitingTeam.set ("Visiting Team")
select_HomeTeam.set ("Home Team")

roster_VisitingTeam = tk.StringVar(screen)
roster_HomeTeam = tk.StringVar(screen)


def getVisitingTeam():
    select_VisitingTeam.get()
    if select_VisitingTeam.get() in options_Teams:
        visitingteam = select_VisitingTeam.get()
        visiting_team_code = team_codes.get(visitingteam)
        print(f'\t{visiting_team_code} is the code for {visitingteam}')
        visitor_stats_file = (f'data/2017_{visiting_team_code}_stats.json')
        data = json.load(open(visitor_stats_file))
        # print (data)

        # FIND PITCHERS
        visiting_pitchers = []
        counter = 0
        for i in range(100):
            try:
                k = data['cumulativeplayerstats']['playerstatsentry'][i]['player']
                if (k["Position"] == "P"):
                    j = {}
                    l = data['cumulativeplayerstats']['playerstatsentry'][i]['team']
                    m = data['cumulativeplayerstats']['playerstatsentry'][i]['stats']
                    j["player"] = k
                    j["team"] = l
                    j["stats"] = m
                    visiting_pitchers.append(j)
                    #print (f'{i} appended')
                    #print (k["LastName"])
                    counter += 1
            except:
                print(f'\nFound  {i-1} players')
                break

        # So now we have a list of all the pitchers
        # print (f'{counter} are pitchers.')
        
        # Initialize a list of ids for players on the 25 man roster
        roster_ids = []
        # Initialize the list of starting pitchers (with stats)
        roster_sp = []
        # Initialize the list of relief pitchers
        roster_rp = []
        # Initialzie the list of middle relief
        roster_midp = []
        


        # SORT by Games Started
        print ("\n5 Starters")
        print ("Starts\tName")
        list = sorted(visiting_pitchers, key=lambda player: int(player["stats"]["GamesStarted"]["#text"]), reverse=True)
        for i in range(5):
            roster_sp.append(list[i])
            visiting_pitchers.remove(list[i])
            roster_ids.append(list[i]["player"]["ID"])
            counter -= 1
            print (f'{list[i]["stats"]["GamesStarted"]["#text"]}\t{list[i]["player"]["LastName"]}')
        #print (list)

        # SORT by Saves
        print ("\n3 Closers")
        print ("Saves\tName")
        list = sorted(visiting_pitchers, key=lambda player: int(player["stats"]["Saves"]["#text"]), reverse=True)
        for i in range(3):
            roster_rp.append(list[i])
            visiting_pitchers.remove(list[i])
            roster_ids.append(list[i]["player"]["ID"])
            counter -= 1
            print(f'{list[i]["stats"]["Saves"]["#text"]}\t{list[i]["player"]["LastName"]}')
        #print(roster_ids)

        # PICK remaining pitchers
        print ("\nOther Pitchers")

        # Remove 4 or more starts from list
        # NOTE: To copy a list, you need the range parameters, otherwise you get a reference to the original not a copy
        list = visiting_pitchers[:]
        for i in range (counter):
            if (int(list[i]["stats"]["GamesStarted"]["#text"]) > 3):
                visiting_pitchers.remove(list[i])
                counter -= 1
        
        # Add from the remaining list based on several factors:
        list = sorted(visiting_pitchers, key=lambda player: float(player["stats"]["InningsPitched"]["#text"]), reverse=True)
        roster_midp.append(list[0])
        visiting_pitchers.remove(list[0])
        roster_ids.append(list[0]["player"]["ID"])
        counter -= 1
        print(f'Added  {list[0]["player"]["LastName"]} for IP')

        list = sorted(visiting_pitchers, key=lambda player: float(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
        roster_midp.append(list[0])
        visiting_pitchers.remove(list[0])
        roster_ids.append(list[0]["player"]["ID"])
        counter -= 1
        print(f'Added  {list[0]["player"]["LastName"]} for GP')

        list = sorted(visiting_pitchers, key=lambda player: float(player["stats"]["Holds"]["#text"]), reverse=True)
        roster_midp.append(list[0])
        visiting_pitchers.remove(list[0])
        roster_ids.append(list[0]["player"]["ID"])
        counter -= 1
        print(f'Added  {list[0]["player"]["LastName"]} for H')

def create_roster_25(select_team, roster):
    #print (select_team)
    #roster.set(select_team) 
    #print (roster.get())
    
    
    if select_team in options_Teams:
        team_roster = select_team
        team_code = team_codes.get(team_roster)
        print(f'\t{team_code} is the code for {team_roster}')
        roster_result = (f'Roster for {team_roster}\n')
        stats_file = (f'data/2017_{team_code}_stats.json')
        data = json.load(open(stats_file))
        # print (data)

        # FIND PITCHERS
        roster_pitchers = []
        counter = 0
        for i in range(100):
            try:
                k = data['cumulativeplayerstats']['playerstatsentry'][i]['player']
                if (k["Position"] == "P"):
                    j = {}
                    l = data['cumulativeplayerstats']['playerstatsentry'][i]['team']
                    m = data['cumulativeplayerstats']['playerstatsentry'][i]['stats']
                    j["player"] = k
                    j["team"] = l
                    j["stats"] = m
                    roster_pitchers.append(j)
                    counter += 1
            except:
                print(f'\nFound  {i-1} players')
                break

        # So now we have a list of all the pitchers
        # print (f'{counter} are pitchers.')
        
        # Initialize a list of ids for players on the 25 man roster
        roster_ids = []
        # Initialize the list of starting pitchers (with stats)
        roster_sp = []
        # Initialize the list of relief pitchers
        roster_rp = []
        # Initialzie the list of middle relief
        roster_midp = []
        
        # SORT by Games Started
        print ("\n5 Starters")
        roster_result += (f'Starting Pitchers\n')

        #print ("Starts\tName")
        list = sorted(roster_pitchers, key=lambda player: int(player["stats"]["GamesStarted"]["#text"]), reverse=True)
        for i in range(5):
            roster_sp.append(list[i])
            roster_pitchers.remove(list[i])
            roster_ids.append(list[i]["player"]["ID"])
            counter -= 1
            print (f'{list[i]["stats"]["GamesStarted"]["#text"]}\t{list[i]["player"]["LastName"]}')
            roster_result += (f'{list[i]["player"]["LastName"]} ({list[i]["stats"]["GamesStarted"]["#text"]})\n')
        #print (list)

        # SORT by Saves
        roster_result += ("Closers\n")
        print ("Saves\tName")
        list = sorted(roster_pitchers, key=lambda player: int(player["stats"]["Saves"]["#text"]), reverse=True)
        for i in range(3):
            roster_rp.append(list[i])
            roster_pitchers.remove(list[i])
            roster_ids.append(list[i]["player"]["ID"])
            counter -= 1
            print(f'{list[i]["stats"]["Saves"]["#text"]}\t{list[i]["player"]["LastName"]}')
            roster_result += (f'{list[i]["player"]["LastName"]}({list[i]["stats"]["Saves"]["#text"]})\n')
        #print(roster_ids)

        # PICK remaining pitchers
        print ("\nOther Pitchers")
        roster_result += ("Bullpen\n")
        

        # Remove 4 or more starts from list
        # NOTE: To copy a list, you need the range parameters, otherwise you get a reference to the original not a copy
        list = roster_pitchers[:]
        for i in range (counter):
            if (int(list[i]["stats"]["GamesStarted"]["#text"]) > 3):
                roster_pitchers.remove(list[i])
                counter -= 1
        
        # Add from the remaining list based on several factors:
        list = sorted(roster_pitchers, key=lambda player: float(player["stats"]["InningsPitched"]["#text"]), reverse=True)
        roster_midp.append(list[0])
        roster_pitchers.remove(list[0])
        roster_ids.append(list[0]["player"]["ID"])
        counter -= 1
        print(f'Added  {list[0]["player"]["LastName"]} for IP')
        roster_result += (f'{list[0]["player"]["LastName"]} ({list[0]["stats"]["InningsPitched"]["#text"]} IP)\n')

        list = sorted(roster_pitchers, key=lambda player: float(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
        roster_midp.append(list[0])
        roster_pitchers.remove(list[0])
        roster_ids.append(list[0]["player"]["ID"])
        counter -= 1
        print(f'Added  {list[0]["player"]["LastName"]} for GP')
        roster_result += (f'{list[0]["player"]["LastName"]} ({list[0]["stats"]["GamesPlayed"]["#text"]} Games)\n')

        list = sorted(roster_pitchers, key=lambda player: float(player["stats"]["Holds"]["#text"]), reverse=True)
        roster_midp.append(list[0])
        roster_pitchers.remove(list[0])
        roster_ids.append(list[0]["player"]["ID"])
        counter -= 1
        print(f'Added  {list[0]["player"]["LastName"]} for H')
        roster_result += (f'{list[0]["player"]["LastName"]} ({list[0]["stats"]["Holds"]["#text"]} Holds)\n')
        # Return the results
        roster.set(roster_result)
        

'''
def getHomeTeam():
    select_HomeTeam.get()
    if select_HomeTeam.get() in options_Teams:
        hometeam = select_HomeTeam.get()
        print (f'{select_HomeTeam.get()} is selected')
        code = team_codes.get(hometeam)
        print (f'{code} is the code for {hometeam}')
'''

visitingteam = tk.OptionMenu(screen, select_VisitingTeam, *visitingteamoptions) 
visitingteam.grid(column=0,row=0)

hometeam = tk.OptionMenu(screen, select_HomeTeam, *hometeamoptions) 
hometeam.grid(column=0,row=1)
#print (hometeam)


#pickvisitingteam = tk.Button(screen, text="OK", command=getVisitingTeam)
pickvisitingteam = tk.Button(screen, text="OK", command=lambda: create_roster_25(select_VisitingTeam.get()))
pickvisitingteam.grid(column=1,row=0)

pickhometeam = tk.Button(screen,text="OK", command= lambda: create_roster_25(select_HomeTeam.get(),roster_HomeTeam))
pickhometeam.grid(column=1,row=1)




# mylabel = tk.Label(screen,textvariable=select_HomeTeam)
# mylabel.grid(column=0,row=2)

homelabel = tk.Label(screen,textvariable=roster_HomeTeam)
homelabel.grid(column=0,row=2)
#mylabel_text = (f'{select_HomeTeam.get()} is Home')
# NO mylabel = tk.Label(screen,textvariable=f'{select_HomeTeam}')
#mylabel = tk.Label(screen,text=mylabel_text)


# Visitor Setup
visiting_team_name = select_VisitingTeam
visitor_pitcher_id ="10719"
visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
visitor_stats_file = "data/2017_nyy_stats.json"

# Find the team stats file
# visiting_team_code =
# Yankees = nyy
# Red Sox = bos
# Phillies = phi
# etc.

# visitor_stats_file =(f'data/2017_{visiting_team_code}_stats.json')

# from that file, need to pull the 9 ids for each position
# Position
# GamesPlayed["#text"]
# GamesStarted
# BatterOnBasePct["#text"]
# BatterSluggingPct["text"]
# BatterOnBasePlusSluggingPct["#text"]
# loop through the positions
# for each group of players at a position, select one based on pct GamesStarted
# when we have a list of 9 players, one for each position, sort into a lineup

# algorithm for that will be something like:
# Slot By
# 3    highest OPS
# 1    highest OBP
# 4    highest SLG
# 2    highest OBP
# 5    highest OPS
# 6-9  highest OBP

# then:
# get another catcher
# get another 1b
# get another of
# get another 2b/ss
# get another 3b

# then:
# get available pitchers
# GamesStarted
# SaveOpportunities
# GamesPlayed
# InningsPitched
# Holds

# Random from available starts
# Relief pitcher with most saveopportunities
# Relief pitcher random by innings
# Relief pitcher random by gamesplayed
# Relief pitcher random by batters faced


screen.mainloop()