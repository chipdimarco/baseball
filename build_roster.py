# Get lists to build teams
# 1/27/2018, rev 2/25/2018

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
    my_roster = buildRoster("2017",t)
    print (my_roster)

def buildRoster(year,team):
    #build active_players list and id_list
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






'''
if __name__ == "__main__":
    main()



v1
def getInfo(team):
    qs = {}
    qs["team"]= team
    return (requests.get(url,headers=headers,params=qs).json())
'''
'''
r = getInfo('bos')
rtext = json.dumps(r)

home_roster = open('home.txt','w')

count = 0
for item in r['activeplayers']['playerentry']:
    lastname = item['player']['LastName']
    firstname  = item['player']['FirstName']
    id = item['player']['ID']
    if count%2:
        print (f'{id}: {lastname}, {firstname}')
        home_roster.write (f'{id}: {lastname}, {firstname}\n')
    count += 1

print ('\nTOTAL IS ' + str(count) + '\n')
home_roster.close()

home_roster = open('home.txt','r')
print (home_roster.readline())
home_roster.close()

#this is dumb but...
r = getInfo('nyy')
rtext = json.dumps(r)

visitor_roster = open('visitor.txt','w')

count = 0
for item in r['activeplayers']['playerentry']:
    lastname = item['player']['LastName']
    firstname  = item['player']['FirstName']
    id = item['player']['ID']
    if count%2:
        print (f'{id}: {lastname}, {firstname}')
        visitor_roster.write (f'{id}: {lastname}, {firstname}\n')
    count += 1

print ('\nTOTAL IS ' + str(count) + '\n')
visitor_roster.close()

visitor_roster = open('visitor.txt','r')
print (visitor_roster.readline())
visitor_roster.close()
'''