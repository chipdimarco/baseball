# 3/20/2018, 3/25/2018

import tkinter as tk
from tkinter import ttk
import json
import random
from game_settings import Settings
from game_lineup import Lineup


# List comprehension will parse out the Keys from this dictionary in Settings
#options_Teams = [i for i in settings.team_codes.keys()]

def create_roster_25(select_team, roster, lineup, settings):
    # if select_team in options_Teams:
    team_roster = select_team
    team_code = settings.team_codes.get(team_roster)
    # print(f'\t{team_code} is the code for {team_roster}')
    roster_result = (f'Roster for {team_roster}\n')
    stats_file = (f'data/2017_{team_code}_stats.json')
    data = json.load(open(stats_file))

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
            #print(f'\nFound  {i-1} players')
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
    # Initialize the list of 9 starters
    lineup_ids = []
    # Initialize the list of bench players
    bench_ids = []
    
    # Now get the positions
    # C
    roster_temp = get_by_postion(data,"C")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_c = []
    roster_c.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_c.append(list[1])
        roster_ids.append(list[1]["player"]["ID"])
        bench_ids.append(list[1]["player"]["ID"])
    for player in roster_c:
        pass
        # print (f'c: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')
    
    # 1b
    roster_temp = get_by_postion(data,"1B")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_1b = []
    roster_1b.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_1b.append(list[1])
        roster_ids.append(list[1]["player"]["ID"])
        bench_ids.append(list[1]["player"]["ID"])
    for player in roster_1b:
        pass
        # print (f'1b: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')
    
    
    roster_temp = get_by_postion(data,"2B")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_2b = []
    roster_2b.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_2b.append(list[1])
        roster_ids.append(list[1]["player"]["ID"])
        bench_ids.append(list[1]["player"]["ID"])
    for player in roster_2b:
        pass
        # print (f'2b: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')
    
    roster_temp = get_by_postion(data,"3B")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_3b = []
    roster_3b.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_3b.append(list[1])
        roster_ids.append(list[1]["player"]["ID"])
        bench_ids.append(list[1]["player"]["ID"])
    for player in roster_3b:
        pass
        # print (f'3b: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')
    
    
    roster_temp = get_by_postion(data,"SS")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_ss = []
    roster_ss.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_ss.append(list[1])
        roster_ids.append(list[1]["player"]["ID"])
        bench_ids.append(list[1]["player"]["ID"])
    for player in roster_ss:
        pass
        # print (f'ss: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')

    roster_of = []
    roster_temp = get_by_postion(data,"LF")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_lf = []
    roster_lf.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_of.append(list[1])
    for player in roster_lf:
        pass
        #print (f'lf: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')
    
    roster_temp = get_by_postion(data,"CF")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_cf = []
    roster_cf.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_of.append(list[1])
    for player in roster_cf:
        pass
        #print (f'cf: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')
    
    roster_temp = get_by_postion(data,"RF")
    list = sorted(roster_temp, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_rf = []
    roster_rf.append(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    lineup_ids.append(list[0]["player"]["ID"])
    if len(list) > 1:
        roster_of.append(list[1])
    for player in roster_rf:
        pass
        # print (f'rf: {player["player"]["LastName"]}')
    roster_result += (f'{list[0]["player"]["LastName"]} - {list[0]["player"]["Position"]}\n')

    # Fourth Outfielder
    list = sorted(roster_of, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_ids.append(list[0]["player"]["ID"])
    bench_ids.append(list[1]["player"]["ID"])
    # SORT by Games Started
    #print ("\n5 Starters")
    roster_result += (f'\nStarting Pitchers\n')

    #print ("Starts\tName")
    list = sorted(roster_pitchers, key=lambda player: int(player["stats"]["GamesStarted"]["#text"]), reverse=True)
    for i in range(5):
        roster_sp.append(list[i])
        roster_pitchers.remove(list[i])
        roster_ids.append(list[i]["player"]["ID"])
        counter -= 1
        # print (f'SP: {list[i]["player"]["LastName"]} (GS: {list[i]["stats"]["GamesStarted"]["#text"]})')
        roster_result += (f'{list[i]["player"]["LastName"]} ({list[i]["stats"]["GamesStarted"]["#text"]})\n')
    #print (list)

    # SORT by Saves
    roster_result += ("Closers\n")
    #print ("Saves\tName")
    list = sorted(roster_pitchers, key=lambda player: int(player["stats"]["Saves"]["#text"]), reverse=True)
    for i in range(3):
        roster_rp.append(list[i])
        roster_pitchers.remove(list[i])
        roster_ids.append(list[i]["player"]["ID"])
        counter -= 1
        # print (f'RP: {list[i]["player"]["LastName"]} (Sv: {list[i]["stats"]["Saves"]["#text"]})')
        roster_result += (f'{list[i]["player"]["LastName"]}({list[i]["stats"]["Saves"]["#text"]})\n')


    # PICK remaining pitchers
    #print ("\nOther Pitchers")
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
    # print(f'RP:  {list[0]["player"]["LastName"]} (IP: {list[0]["stats"]["InningsPitched"]["#text"]})')
    roster_result += (f'{list[0]["player"]["LastName"]} ({list[0]["stats"]["InningsPitched"]["#text"]} IP)\n')

    list = sorted(roster_pitchers, key=lambda player: float(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    roster_midp.append(list[0])
    roster_pitchers.remove(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    counter -= 1
    # print(f'RP:  {list[0]["player"]["LastName"]} (GP: {list[0]["stats"]["GamesPlayed"]["#text"]})')
    roster_result += (f'{list[0]["player"]["LastName"]} ({list[0]["stats"]["GamesPlayed"]["#text"]} Games)\n')

    list = sorted(roster_pitchers, key=lambda player: float(player["stats"]["Holds"]["#text"]), reverse=True)
    roster_midp.append(list[0])
    roster_pitchers.remove(list[0])
    roster_ids.append(list[0]["player"]["ID"])
    counter -= 1
    # print(f'RP:  {list[0]["player"]["LastName"]} (H: {list[0]["stats"]["Holds"]["#text"]})')
    roster_result += (f'{list[0]["player"]["LastName"]} ({list[0]["stats"]["Holds"]["#text"]} Holds)\n')
    
    # Pick Starter
    starting_pitcher = random.choice(roster_sp)
    starting_pitcher_id = starting_pitcher["player"]["ID"]
    # print (f'{starting_pitcher["player"]["LastName"]} ({starting_pitcher_id})')
    lineup.pitcher = starting_pitcher

    # Pick DH
    # print (f'Bench IDs: {bench_ids}')
    if (settings.use_dh):
        dh = select_dh(data,bench_ids)
        lineup_ids.append(dh)
    else:
        lineup_ids.append(starting_pitcher["player"]["ID"])
    # print (f'Lineup IDs: {lineup_ids}')

    '''
    # Initialize a list of ids for players on the 25 man roster
    roster_ids = []
    # Initialize the list of starting pitchers (with stats)
    roster_sp = []
    # Initialize the list of relief pitchers
    roster_rp = []
    # Initialzie the list of middle relief
    roster_midp = []
    # Initialize the list of 9 starters
    lineup_ids = []
    # Initialize the list of bench players
    bench_ids = []
    '''
    order_ids = batting_order(data,lineup_ids,lineup)


    lineup.roster_ids = roster_ids
    lineup.roster_result = roster_result
    lineup.lineup_dictionary = lineup.create_lineup_dictionary_from_file(stats_file,order_ids)
    lineup.battingorder_result += (f'\n\nStarting Pitcher: {starting_pitcher["player"]["LastName"]}')

    return(roster_result)
    

    # stuff = {}
    # stuff["roster_ids"] = roster_ids
    # stuff["lineup_ids"] = lineup_ids
    # stuff["bench_ids"] = bench_ids
    # stuff["order_ids"] = order_ids

    # roster.set(roster_result)
    # stuff["roster_result"] = roster.set(roster_result)

    # return(stuff)
    # return (order_ids)

def select_dh(data, bench_players):
    # Init lineup as dictionary
    r = data
    bench_stats = []
    # loop over dict. to retrieve stats
    for i in range (100):
        try:
            if data['cumulativeplayerstats']['playerstatsentry'][i]['player']['ID'] in bench_players:
                j = {}
                k = data['cumulativeplayerstats']['playerstatsentry'][i]['player']
                l = data['cumulativeplayerstats']['playerstatsentry'][i]['team']
                m = data['cumulativeplayerstats']['playerstatsentry'][i]['stats']
                j["player"] = k
                j["team"] = l
                j["stats"] = m
                bench_stats.append(j)
        except:
            break
    
    # Select Games Played max from the list
    list = sorted(bench_stats, key=lambda player: int(player["stats"]["GamesPlayed"]["#text"]), reverse=True)
    #print (list[0]['player']['LastName'])
    return (list[0]['player']['ID'])

def get_by_postion(data, pos):
    roster_pos = []
    pos_counter = 0
    for i in range (100):
        try:
            k = data['cumulativeplayerstats']['playerstatsentry'][i]['player']
            if (k["Position"] == pos ):
                j = {}
                l = data['cumulativeplayerstats']['playerstatsentry'][i]['team']
                m = data['cumulativeplayerstats']['playerstatsentry'][i]['stats']
                j["player"] = k
                j["team"] = l
                j["stats"] = m
                roster_pos.append(j)
                pos_counter += 1
                #print(f'\n{pos}: {j["player"]["LastName"]}')
        except:
            break
    return (roster_pos)

def batting_order(data,lineup_ids,lineup):
    # Init lineup as dictionary
    r = data
    batters = []
    battingorder_result = "Starting Lineup\n"
    # loop over dict. to retrieve stats
    for i in range (100):
        try:
            if data['cumulativeplayerstats']['playerstatsentry'][i]['player']['ID'] in lineup_ids:
                j = {}
                k = data['cumulativeplayerstats']['playerstatsentry'][i]['player']
                l = data['cumulativeplayerstats']['playerstatsentry'][i]['team']
                m = data['cumulativeplayerstats']['playerstatsentry'][i]['stats']
                j["player"] = k
                j["team"] = l
                j["stats"] = m
                batters.append(j)
        except:
            break
    
    battingorder_ids = []
    # Select 
    list = sorted(batters, key=lambda player: float(player["stats"]["BatterOnBasePlusSluggingPct"]["#text"]), reverse=True)
    bo3 = list[0]
    battingorder_ids.append(list[0]['player']['ID'])
    batters.remove(bo3)
    battingorder_result += (f'{list[0]["player"]["LastName"]} ({list[0]["player"]["Position"]})\n')
    
    list = sorted(batters, key=lambda player: float(player["stats"]["BatterOnBasePct"]["#text"]), reverse=True)
    bo1 = list[0]
    battingorder_ids.append(list[0]['player']['ID'])
    batters.remove(bo1)
    battingorder_result += (f'{list[0]["player"]["LastName"]} ({list[0]["player"]["Position"]})\n')

    list = sorted(batters, key=lambda player: float(player["stats"]["BatterSluggingPct"]["#text"]), reverse=True)
    bo4 = list[0]
    battingorder_ids.append(list[0]['player']['ID'])
    batters.remove(bo4)
    battingorder_result += (f'{list[0]["player"]["LastName"]} ({list[0]["player"]["Position"]})\n')
    
    list = sorted(batters, key=lambda player: float(player["stats"]["BatterOnBasePct"]["#text"]), reverse=True)
    bo2 = list[0]
    battingorder_ids.append(list[0]['player']['ID'])
    batters.remove(bo2)
    battingorder_result += (f'{list[0]["player"]["LastName"]} ({list[0]["player"]["Position"]})\n')
    
    list = sorted(batters, key=lambda player: float(player["stats"]["BatterOnBasePlusSluggingPct"]["#text"]), reverse=True)
    bo5 = list[0]
    battingorder_ids.append(list[0]['player']['ID'])
    batters.remove(bo5)
    battingorder_result += (f'{list[0]["player"]["LastName"]} ({list[0]["player"]["Position"]})\n')

    #6-9    
    list = sorted(batters, key=lambda player: float(player["stats"]["BatterSluggingPct"]["#text"]), reverse=True)
    bo6 = list[0]
    battingorder_ids.append(list[0]['player']['ID'])
    battingorder_result += (f'{list[0]["player"]["LastName"]} ({list[0]["player"]["Position"]})\n')
    bo7 = list[1]
    battingorder_ids.append(list[1]['player']['ID'])
    battingorder_result += (f'{list[1]["player"]["LastName"]} ({list[1]["player"]["Position"]})\n')
    bo8 = list[2]
    battingorder_ids.append(list[2]['player']['ID'])
    battingorder_result += (f'{list[2]["player"]["LastName"]} ({list[2]["player"]["Position"]})\n')
    bo9 = list[3]
    battingorder_ids.append(list[3]['player']['ID'])
    battingorder_result += (f'{list[3]["player"]["LastName"]} ({list[3]["player"]["Position"]})\n')


    '''
    print (bo1['player']['LastName'])
    print (bo2['player']['LastName'])
    print (bo3['player']['LastName'])
    print (bo4['player']['LastName'])
    print (bo5['player']['LastName'])
    print (bo6['player']['LastName'])
    print (bo7['player']['LastName'])
    print (bo8['player']['LastName'])
    print (bo9['player']['LastName'])
    '''
    lineup.battingorder_result = battingorder_result
    
    # print (list[0]['player']['LastName'])
    return (battingorder_ids)
    

