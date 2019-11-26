# Get a list of players with ids
# 1/27/2018

# import
import requests
import json
import os
import base64
import random


# environment variables"

# environment variables"
api_url  = "https://api.mysportsfeeds.com/v1.2/pull/mlb/2019-regular/cumulative_player_stats.json"
api_password = os.environ["API_PASSWORD"]
api_key = os.environ["API_KEY"]
api_msf = os.environ["MSF_KEY"]

team = "HOU"
year = "2019"
#auth = os.environ['API_KEY']
#url = "https://api.mysportsfeeds.com/v1.2/pull/mlb/2019-regular/active_players.json"
#headers = {
#    'Authorization': "Basic " + auth
#    }


response = requests.get(
    url = api_url,
    params = {
        'team':team
        },
    headers = {
#        "Authorization" : "Basic " + base64.b64encode('{}:{}'.format({api_key}, {api_password}).encode('utf-8')).decode('ascii')
        "Authorization" : "Basic " + base64.b64encode('30f6f039-cd9e-42e7-889f-340515:phantoM9'.encode('utf-8')).decode('ascii')
    }
)

#print ( response.content )

r = response.content
rtext = json.loads(r)

#bbdata = rtext["cumulativeplayerstats"]["playerstatsentry"]

bbdata = json.dumps(rtext)
#exit()
#rtext = json.dumps(r)
roster_file = open(f'{year}-{team}.json','w')
roster_file.write(bbdata)
roster_file.close()
print ("done")
exit()


def getInfo2017(team):
    qs = {}
    qs["team"]= team
    return (requests.get(url,headers=headers,params=qs).json())

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
