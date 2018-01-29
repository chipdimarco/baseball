# Get a list of players with ids
# 1/27/2018

# import
import requests
import json
import os

# environment variables"
auth = os.environ['MSF_KEY']
url = "https://api.mysportsfeeds.com/v1.2/pull/mlb/2017-regular/active_players.json"
headers = {
    'Authorization': "Basic " + auth
    }

def getInfo(team):
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
