# Get lists to build teams
# 1/27/2018, rev 2/25/2018
# revised 9/28/2019
# tweaks 11/21/2019

# import
import requests
import json
import os
import base64
import random

# environment variables"
api_url  = "https://api.mysportsfeeds.com/v1.2/pull/mlb/2019-regular/cumulative_player_stats.json"
api_password = os.environ["API_PASSWORD"]
api_key = os.environ["API_KEY"]
api_msf = os.environ["MSF_KEY"]


### FUNCTIONS
def send_request(team):
    try:
        response = requests.get(
            url = api_url,
            params = {'team':team},
            headers = {
                "Authorization" : "Basic " + base64.b64encode('{}:{}'.format(api_key,api_password).encode('utf-8')).decode('ascii')
            }
        )
        rtext = response.json()
        currentseason_file = f'2018-{team}.json'
        currentseason = open(currentseason_file, 'w')
        currentseason.write(json.dumps(rtext))
        currentseason.close()
        return (f'{currentseason_file} done') 
    except requests.exceptions.RequestException:
        print ('HTTP Request Failed')

def roster(stats_file):
    r = json.load(stats_file)
    result = []
    for item in r["cumulativeplayerstats"]["playerstatsentry"]:
        lastname = item['player']['LastName']
        firstname  = item['player']['FirstName']
        id = item['player']['ID']
        position = item['player']['Position']
        result.append(f'{id}: {position} {lastname}, {firstname}')
    return (result)

def read_roster_dict(stats_file):
    r = json.load(stats_file)
    result = []
    for item in r["cumulativeplayerstats"]["playerstatsentry"]:
        result.append(item)
    return(result)

def build_game_roster(team, year):
    team = team
    year = year
    folder_name = 'mlbstats/'
    file_name   = f'{folder_name}{year}-{team}.json'
    stats       = open(file_name,'r')
    roster      = read_roster_dict(stats)
    game_roster = []
    for item in roster:
        new_player = {}
        new_player["FirstName"] = item["player"]["FirstName"]
        new_player["LastName"]  = item["player"]["LastName"]
        new_player["ID"]        = item['player']['ID']
        new_player["Position"]  = item['player']['Position']
        new_player["G"]         = int(item['stats']['GamesPlayed']['#text'])
        new_player["AB"]        = int(item['stats']['AtBats']['#text'])
        new_player["2B"]        = int(item['stats']['SecondBaseHits']['#text'])
        new_player["3B"]        = int(item['stats']['ThirdBaseHits']['#text'])
        new_player["HR"]        = int(item['stats']['Homeruns']['#text'])
        hits         = int(item['stats']['Hits']['#text'])
        new_player["H"]         = int(item['stats']['Hits']['#text'])
        new_player["1B"]        = hits - new_player["2B"] - new_player["3B"] - new_player["HR"]
        new_player["RBI"]       = int(item['stats']['RunsBattedIn']['#text'])
        new_player["BB"]        = int(item['stats']['BatterWalks']['#text'])
        new_player["SO"]        = int(item['stats']['BatterStrikeouts']['#text'])
        new_player["SB"]        = int(item['stats']['StolenBases']['#text'])

        new_player["GO"]        = int(item['stats']['BatterGroundOuts']['#text'])
        new_player["FO"]        = int(item['stats']['BatterFlyOuts']['#text'])

        new_player["CS"]        = int(item['stats']['CaughtBaseSteals']['#text'])
        new_player["GS"]        = int(item['stats']['GamesStarted']['#text'])
        new_player["E"]         = int(item['stats']['Errors']['#text'])
        new_player["HBP"]       = int(item['stats']['HitByPitch']['#text'])
        new_player["AVG"]       = round( float ( item['stats']['BattingAvg']['#text']), 3)
        new_player["OBP"]       = round( float ( item['stats']['BatterOnBasePct']['#text']), 3)
        new_player["SLG"]       = round( float ( item['stats']['BatterSluggingPct']['#text']), 3)
        new_player["OPS"]       = round( float ( item['stats']['BatterOnBasePlusSluggingPct']['#text']), 3)
        new_player["PA"]        = int(item['stats']['PlateAppearances']['#text'])
        if new_player["Position"] == "P":
            new_player["TBF"]       = int(item['stats']['TotalBattersFaced']['#text'])
            new_player["W"]         = int(item['stats']['Wins']['#text'])
            new_player["L"]         = int(item['stats']['Losses']['#text'])
            new_player["SV"]        = int(item['stats']['Saves']['#text'])
            new_player["IP"]        = int( float (item['stats']['InningsPitched']['#text']))
            new_player["2BA"]       = int(item['stats']['SecondBaseHitsAllowed']['#text'])
            new_player["3BA"]       = int(item['stats']['ThirdBaseHitsAllowed']['#text'])
            new_player["HRA"]       = int(item['stats']['HomerunsAllowed']['#text'])
            hitsallowed             = int(item['stats']['HitsAllowed']['#text'])
            new_player["HA"]        = int(item['stats']['HitsAllowed']['#text'])
            new_player["1BA"]       = hitsallowed - new_player["2BA"] - new_player["3BA"] - new_player["HRA"]
            new_player["BBA"]       = int(item['stats']['PitcherWalks']['#text'])
            new_player["K"]         = int(item['stats']['PitcherStrikeouts']['#text'])
            new_player["PGO"]       = int(item['stats']['PitcherGroundOuts']['#text'])
            new_player["PFO"]       = int(item['stats']['PitcherFlyOuts']['#text'])
            new_player["HB"]        = int(item['stats']['BattersHit']['#text'])
        game_roster.append(new_player)
    stats.close()
    return(game_roster)

def pick_starters_dh(roster):
    starters = []
    for x in ["C","1B","2B","3B","SS","LF","CF","RF"]:
        p = []
        for i in roster:
            if i["Position"] == x:
                gs = i["GS"]
                for n in range (gs):
                    p.append(i)
        starter = random.choice(p)
        starters.append(starter)
        roster.remove(starter)

    dhs = []
    max_gs = 0
    for j in roster:
        if j["Position"] != "P" and j["GS"] > max_gs:
            starter = j
            max_gs = j["GS"]
    dhs.append(starter)

    max_ops = 0
    for j in roster:
        if j["Position"] != "P" and j["OPS"] > max_ops:
            starter = j
            max_ops = j["OPS"]
    dhs.append(starter)

    max_obp = 0
    for j in roster:
        if j["Position"] != "P" and j["OBP"] > max_obp:
            starter = j
            max_obp = j["OBP"]
    dhs.append(starter)

    j = []
    for dh in dhs:
        for x in range(dh["GS"]):
            j.append(dh)
    starter = random.choice(j)

    starter["Position"] = "DH"
    starters.append(starter)
    roster.remove(starter)
    #
    # Now get Pitchers
    all_pitchers = []
    five_starting_pitchers = []
    five_relief_pitchers = []
    starting_pitchers = []
    for i in roster:
        if i["Position"] == "P":
            all_pitchers.append(i)             
    for i in all_pitchers:
        if i["Position"] == "P" and i["GS"] > 0:
            starting_pitchers.append(i)             
    # get five guys with starts
    for counter in range(5):
        j = []
        for sp in starting_pitchers:
            for x in range(sp["GS"]):
                j.append(sp)
        starter = random.choice(j)
        # print (f'SP{counter} - {starter["LastName"]}')
        five_starting_pitchers.append(starter)
        all_pitchers.remove(starter)
        starting_pitchers.remove(starter)
        roster.remove(starter)
    #
    # get two guys with saves
    for counter in range(2):
        j = []
        for p in all_pitchers:
            if p["SV"] > 0:
                for x in range(p["SV"]):
                    j.append(p)
        try:
            starter = random.choice(j)
            # print (f'Closer{counter} - {starter["LastName"]}')
            five_relief_pitchers.append(starter)
            all_pitchers.remove(starter)
            roster.remove(starter)
        except:
            pass
    # get three other relief pitchers
    # more if we didn't get two closers
    add_to_roster = 5 - len(five_relief_pitchers)    
    for counter in range(add_to_roster):
        j = []
        for p in all_pitchers:
            if p["Position"] == "P" and p["G"] - p["GS"] > 0:
                for x in range(p["G"] - p["GS"]):
                    j.append(p)
        starter = random.choice(j)
        # print (f'Bullpen{counter} - {starter["LastName"]}')
        five_relief_pitchers.append(starter)
        all_pitchers.remove(starter)
        roster.remove(starter)
    # get 6 bench players
    bench = []
    # get another catcher
    j = []
    for pos in roster:
        if pos["Position"] == "C":
            for x in range(pos["GS"]):
                j.append(pos)
    try:
        starter = random.choice(j)
        bench.append(starter)
        roster.remove(starter)
    except:
        pass
    # get a corner infielder
    j = []
    for pos in roster:
        if pos["Position"] == "3B" or pos["Position"] == "1B":
            for x in range(pos["G"]):
                j.append(pos)
    try:
        starter = random.choice(j)
        bench.append(starter)
        roster.remove(starter)
    except:
        pass
    # get a middle infielder
    j = []
    for pos in roster:
        if pos["Position"] in ( "SS", "2B" ):
            for x in range(pos["G"]):
                j.append(pos)
    # NOTE - HOU ERROR HERE where list was empty 
    try:
        starter = random.choice(j)
        bench.append(starter)
        roster.remove(starter)
    except:
        pass
    # get an outfielder
    j = []
    for pos in roster:
        if pos["Position"] in ["LF","CF","RF"]:
            for x in range(pos["G"]):
                j.append(pos)
    starter = random.choice(j)
    bench.append(starter)
    roster.remove(starter)
    # get another outfielder
    j = []
    for pos in roster:
        if pos["Position"] in ["LF","CF","RF"]:
            for x in range(pos["G"]):
                j.append(pos)
    try:
        starter = random.choice(j)
        bench.append(starter)
        roster.remove(starter)
    except:
        pass
    # get another infielder
    j = []
    for pos in roster:
        if pos["Position"] in ["1B","2B","3B","SS"]:
            for x in range(pos["G"]):
                j.append(pos)
    try:
        starter = random.choice(j)
        bench.append(starter)
        roster.remove(starter)
    except:
        pass
    # Check here for enough players
    # if the len is wrong, pick random from remaining
    for counter in range(6 - len(bench)):
        starter = random.choice(roster)
        bench.append(starter)
        roster.remove(starter)
    #
    response = {}
    response["lineup"]=starters
    response["rotation"]=five_starting_pitchers
    response["bullpen"]=five_relief_pitchers
    response["bench"]=bench
    return (response)

def pick_starters(roster):
    starters = []
    for x in ["C","1B","2B","3B","SS","LF","CF","RF"]:
        p = []
        for i in roster:
            if i["Position"] == x:
                gs = i["GS"]
                for n in range (gs):
                    p.append(i)
        starters.append(random.choice(p))
    # sort pitchers
    pitchers = []
    for i in roster:
        if i["Position"] == "P":
            pitchers.append(i)
    p = []
    for pitcher in pitchers:
        if pitcher["GS"] > 0:
            for n in range (pitcher["GS"]):
                p.append(pitcher)
    startingpitcher = random.choice(p)
    response = {}
    response["starters"] = starters
    return (response)

def make_battingorder(starters, dh):
    battingorder = []
    # 3 - Select max OBS 
    list = sorted(starters, key=lambda player: float(player["OPS"]), reverse=True)
    bo3 = list[0]
    bo3["bo"] = 3
    starters.remove(bo3)
    # 1 - Select max OBP 
    list = sorted(starters, key=lambda player: float(player["OBP"]), reverse=True)
    bo1 = list[0]
    bo1["bo"] = 1
    starters.remove(bo1)
    # 4 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo4 = list[0]
    bo4["bo"] = 4
    starters.remove(bo4)
    # 2 - Select max OBP 
    list = sorted(starters, key=lambda player: float(player["OBP"]), reverse=True)
    bo2 = list[0]
    bo2["bo"] = 2
    starters.remove(bo2)
    # 5 - Select max OBS 
    list = sorted(starters, key=lambda player: float(player["OPS"]), reverse=True)
    bo5 = list[0]
    bo5["bo"] = 5
    starters.remove(bo5)
    # 6 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo6 = list[0]
    bo6["bo"] = 6
    starters.remove(bo6)
    # 7 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo7 = list[0]
    bo7["bo"] = 7
    starters.remove(bo7)
    # 8 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo8 = list[0]
    bo8["bo"] = 8
    starters.remove(bo8)
    battingorder.append(bo1)
    battingorder.append(bo2)
    battingorder.append(bo3)
    battingorder.append(bo4)
    battingorder.append(bo5)
    battingorder.append(bo6)
    battingorder.append(bo7)
    battingorder.append(bo8)
    if dh == True:
        bo9 = list[1]
        bo9["bo"] = 9
        battingorder.append(bo9)
    return (battingorder)

def pick_starting_pitcher(rotation):
    return (random.choice(rotation))


def pick_starters_dh_v1(roster):
    starters = []
    for x in ["C","1B","2B","3B","SS","LF","CF","RF"]:
        p = []
        for i in roster:
            if i["Position"] == x:
                gs = i["GS"]
                for n in range (gs):
                    p.append(i)
        starter = random.choice(p)
        starters.append(starter)
        roster.remove(starter)

    dhs = []
    max_gs = 0
    for j in roster:
        if j["Position"] != "P" and j["GS"] > max_gs:
            starter = j
            max_gs = j["GS"]
    dhs.append(starter)

    max_ops = 0
    for j in roster:
        if j["Position"] != "P" and j["OPS"] > max_ops:
            starter = j
            max_ops = j["OPS"]
    dhs.append(starter)

    max_obp = 0
    for j in roster:
        if j["Position"] != "P" and j["OBP"] > max_obp:
            starter = j
            max_obp = j["OBP"]
    dhs.append(starter)

    j = []
    for dh in dhs:
        for x in range(dh["GS"]):
            j.append(dh)
    starter = random.choice(j)

    starter["Position"] = "DH"
    starters.append(starter)             
    return (starters)
