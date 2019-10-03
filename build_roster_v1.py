# Get lists to build teams
# 1/27/2018, rev 2/25/2018
# revised 9/28/2019

# import
import requests
import json
import os


# environment variables"
auth = os.environ['MSF_KEY']
headers = {
    'Authorization': "Basic " + auth
    }

# define the MLB teams to get
mlbteams = ("bos","nyy","tb","hou","chc","phi")
# loop through the tuple, creating the three files for each
for t in mlbteams:
    my_roster = buildRoster("2018",t)
    print (my_roster)

def get_currentseason():
    url = "https://api.mysportsfeed.com/v2.1/pull/mlb/currentseason.json"
    r = requests.get(url,headers=headers).json()
    rtext = json.dumps(r)
    currentseason_file = 'currentseason.json'
    currentseason = open(currentseason_file, 'w')
    currentseason.write (rtext)
    currentseason_file.close()

def buildRoster(year,team):
    #BUILD ACTIVE_PLAYERS LIST AND ID_LIST
    url = "https://api.mysportsfeeds.com/v1.2/pull/mlb/" + year + "-regular/active_players.json"
    url = "https://api.mysportsfeeds.com/v1.2/pull/mlb/" + year + "-regular/active_players.json"
    query_string = {}
    query_string["team"]=team
    # request
    r = requests.get(url,headers=headers,params=query_string).json()
    # parse to files
    rtext = json.dumps(r)

    #active_players
    active_players_file = (f'{year}_{team}_activeplayers.json')
    active_players = open(active_players_file, 'w')
    active_players.write(rtext)
    active_players.close()

    #id_list
    id_list_file = (f'{year}_{team}_id_list.txt')
    id_list = open(id_list_file,'w')

    count = 0
    for item in r['activeplayers']['playerentry']:
        lastname = item['player']['LastName']
        firstname  = item['player']['FirstName']
        id = item['player']['ID']
        print (f'{id}: {lastname}, {firstname}')
        id_list.write (f'{id}: {lastname}, {firstname}\n')
        count += 1

    # then build stats list
    #stats
    url = "https://api.mysportsfeeds.com/v1.2/pull/mlb/" + year + "-regular/cumulative_player_stats.json"
    query_string = {}
    query_string["team"]=team
    #request
    r = requests.get(url,headers=headers,params=query_string).json()
    rtext = json.dumps(r)
    #
    stats_file = (f'{year}_{team}_stats.json')
    stats = open(stats_file,'w')
    stats.write(rtext)
    stats.close()
        
    id_list.close()
    return("done")

