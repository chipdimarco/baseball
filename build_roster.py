# Get lists to build teams
# 1/27/2018, rev 2/25/2018
# revised 9/28/2019

# import
import requests
import json
import os
import base64
import random

# environment variables"
api_url  = "https://api.mysportsfeeds.com/v1.2/pull/mlb/2018-regular/cumulative_player_stats.json"
api_password = os.environ["API_PASSWORD"]
api_key = os.environ["API_KEY"]

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
    file_name   = f'{year}-{team}.json'
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
        new_player["1B"]        = hits - new_player["2B"] - new_player["3B"] - new_player["HR"]
        new_player["RBI"]       = int(item['stats']['RunsBattedIn']['#text'])
        new_player["BB"]        = int(item['stats']['BatterWalks']['#text'])
        new_player["SO"]        = int(item['stats']['BatterStrikeouts']['#text'])
        new_player["SB"]        = int(item['stats']['BatterStrikeouts']['#text'])
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
            new_player["2BA"]       = int(item['stats']['SecondBaseHitsAllowed']['#text'])
            new_player["3BA"]       = int(item['stats']['ThirdBaseHitsAllowed']['#text'])
            new_player["HRA"]       = int(item['stats']['HomerunsAllowed']['#text'])
            hitsallowed             = int(item['stats']['HitsAllowed']['#text'])
            new_player["1BA"]       = hitsallowed - new_player["2BA"] - new_player["3BA"] - new_player["HRA"]
            new_player["BBA"]       = int(item['stats']['PitcherWalks']['#text'])
            new_player["K"]         = int(item['stats']['PitcherStrikeouts']['#text'])
            new_player["HB"]        = int(item['stats']['BattersHit']['#text'])
        game_roster.append(new_player)
    stats.close()
    return(game_roster)


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
    return (starters)

def make_battingorder(starters):
    battingorder = []
    # 3 - Select max OBS 
    list = sorted(starters, key=lambda player: float(player["OPS"]), reverse=True)
    bo3 = list[0]
    starters.remove(bo3)
    # 1 - Select max OBP 
    list = sorted(starters, key=lambda player: float(player["OBP"]), reverse=True)
    bo1 = list[0]
    starters.remove(bo1)
    # 4 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo4 = list[0]
    starters.remove(bo4)
    # 2 - Select max OBP 
    list = sorted(starters, key=lambda player: float(player["OBP"]), reverse=True)
    bo2 = list[0]
    starters.remove(bo2)
    # 5 - Select max OBS 
    list = sorted(starters, key=lambda player: float(player["OPS"]), reverse=True)
    bo5 = list[0]
    starters.remove(bo5)
    # 6 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo6 = list[0]
    starters.remove(bo6)
    # 7 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo7 = list[0]
    starters.remove(bo7)
    # 8 - Select max SLG 
    list = sorted(starters, key=lambda player: float(player["SLG"]), reverse=True)
    bo8 = list[0]
    starters.remove(bo8)
    battingorder.append(bo1)
    battingorder.append(bo2)
    battingorder.append(bo3)
    battingorder.append(bo4)
    battingorder.append(bo5)
    battingorder.append(bo6)
    battingorder.append(bo7)
    battingorder.append(bo8)
    return (battingorder)


### PROCEDURE
v_roster = build_game_roster('HOU','2018')
h_roster = build_game_roster('BOS','2018')

v_starters = pick_starters(v_roster)
h_starters = pick_starters(h_roster)

print(f'Starters')
print(f'Visitors')
for x in v_starters:
    print (f'{x["Position"]}: {x["LastName"]}')

print (f'\nHome')
for x in h_starters:
    print (f'{x["Position"]}: {x["LastName"]}')

print(f'\nBatting Order')
print(f'Visitors')

v_battingorder = make_battingorder(v_starters)
for x in v_battingorder:
    print (f'{x["Position"]}: {x["LastName"]}')

print(f'\nHome')
h_battingorder = make_battingorder(h_starters)
for x in h_battingorder:
    print (f'{x["Position"]}: {x["LastName"]}')

exit()