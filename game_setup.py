# 3/20/2018

import tkinter as tk
from tkinter import ttk
import json

screen = tk.Tk()
screen.title("Testing")
screen_width=900
screen_height=600
screen.geometry(f'{screen_width}x{screen_height}')
#screen.configure(background="#e8e8e8")
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
#hometeamoptions = [i for i in options_Teams if i != select_VisitingTeam]
select_VisitingTeam.set ("Visiting Team")
select_HomeTeam.set ("Home Team")

def getVisitingTeam():
    select_VisitingTeam.get()
    if select_VisitingTeam.get() in options_Teams:
        visitingteam = select_VisitingTeam.get()
        visiting_team_code = team_codes.get(visitingteam)
        print(f'{visiting_team_code} is the code for {visitingteam}')
        visitor_stats_file = (f'data/2017_{visiting_team_code}_stats.json')
        data = json.load(open(visitor_stats_file))
        print (data)
        # find the pitchers
        visiting_pitchers = []
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
                    print (k["LastName"])
                    #break
            except:
                print(f'error finding {i}')
                break


def getHomeTeam():
    select_HomeTeam.get()
    if select_HomeTeam.get() in options_Teams:
        hometeam = select_HomeTeam.get()
        print (f'{select_HomeTeam.get()} is selected')
        code = team_codes.get(hometeam)
        print (f'{code} is the code for {hometeam}')


visitingteam = tk.OptionMenu(screen, select_VisitingTeam, *visitingteamoptions) 
visitingteam.grid(column=0,row=0)

hometeam = tk.OptionMenu(screen, select_HomeTeam, *hometeamoptions) 
hometeam.grid(column=0,row=1)
#print (hometeam)


pickvisitingteam = tk.Button(screen, text="OK", command=getVisitingTeam)
pickvisitingteam.grid(column=1,row=0)

pickhometeam = tk.Button(screen,text="OK", command= getHomeTeam)
pickhometeam.grid(column=1,row=1)




mylabel = tk.Label(screen,textvariable=select_HomeTeam)
mylabel.grid(column=0,row=2)
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