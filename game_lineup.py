# generates lineups from a list of player ids
# 1/28/2018 v1
# class Lineup creates the lineup object
# method create_lineup_dictionary() is called from app with a parameter of selected player ids
# returns the python dict string over which the gameplay will loop 

import json
import requests
import os

# environment variables"
auth = os.environ['MSF_KEY']
url = "https://api.mysportsfeeds.com/v1.2/pull/mlb/2017-regular/cumulative_player_stats.json"
headers = {
    'Authorization': "Basic " + auth
    }

class Lineup():
    def __init__(self):
        self.note = "lineup"
    
    def getInfo(self,id):
        self.id = id
        qs = {}
        qs["player"]=id
        return (requests.get(url,headers=headers,params=qs).json())


    # Method for creating a lineup with stats from a dict. of ids
    def create_lineup_dictionary(self,ids):
        self.ids = ids
        '''
        def getInfo(id):
            qs = {}
            qs["player"]=id
            return (requests.get(url,headers=headers,params=qs).json())
        '''

        # Init lineup
        # lineup = {}
        # As list
        lineup = []
        # loop over dict. to retrieve stats
        for id in ids:
            r = self.getInfo(id)
            j = {}
            j['id'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['ID']
            j['firstname'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['FirstName']
            j['lastname'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['LastName']
            j['atbats'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['AtBats']['#text']
            j['gamesplayed'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['GamesPlayed']['#text']
            j['plateappearances'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['PlateAppearances']['#text']
            j['bb'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['BatterWalks']['#text']
            j['hits'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['Hits']['#text']
            j['secondbasehits'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['SecondBaseHits']['#text']
            j['thirdbasehits'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['ThirdBaseHits']['#text']
            j['homeruns'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['Homeruns']['#text']

            # add the subdictionary to the main dictionary
            #lineup[id]=j
            #lineup.update(j)
            lineup.append(j)

        # return the lineup
        return (lineup)

    def lineup_lastname(self, lineup_dictionary):
        self.lineup_dictionary = lineup_dictionary
        lineup = []
        for i in range ( 0, len(lineup_dictionary)):
            lineup.append(lineup_dictionary[i]["lastname"])
        return (lineup)

    def get_pitcher(self,id):
        self.id = id
        r = self.getInfo(id)
        j = {}
        # parse out r into j
        j['id'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['ID']
        j['firstname'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['FirstName']
        j['lastname'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['LastName']
        j['totalbattersfaced'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['TotalBattersFaced']['#text']
        j['hitsallowed'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['HitsAllowed']['#text']
        j['pitcherstrikeouts'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['PitcherStrikeouts']['#text']
        j['pitcherwalks'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['PitcherWalks']['#text']
        j['secondbasehitsallowed'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['SecondBaseHitsAllowed']['#text']
        j['thirdbasehitsallowed'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['ThirdBaseHitsAllowed']['#text']
        j['homerunsallowed'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['HomerunsAllowed']['#text']
        
        return (j)



'''
# ids
# example array
ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
# this is the array that lineup will take as its parameter
# test for length = 9, each is a valid id.

# Call Info for the Lineup from url
# method
def getInfo(id):
    qs = {}
    qs["player"]= id
    return (requests.get(url,headers=headers,params=qs).json())

# variables for loop
count = 0
# init python dict
lineup = {}

# loop through the array of ids
for id in ids:
    # get the id and call info from url
    r = getInfo(id)

    # start a new dictionary
    j = {}

    # grab just what we want from the data set
    j['firstname'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['FirstName']
    j['lastname'] = r['cumulativeplayerstats']['playerstatsentry'][0]['player']['LastName']
    j['atbats'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['AtBats']['#text']
    j['gamesplayed'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['GamesPlayed']['#text']
    j['plateappearances'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['PlateAppearances']['#text']
    j['bb'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['BatterWalks']['#text']
    j['hits'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['Hits']['#text']
    j['secondbasehits'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['SecondBaseHits']['#text']
    j['thirdbasehits'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['ThirdBaseHits']['#text']
    j['homeruns'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['Homeruns']['#text']

    # add the subdictionary to the main dictionary
    lineup[id]=j

# OUTPUT
# print (json.dumps(lineup))
# print (lineup)
# print (json.dumps(lineup, indent=1))
pprint.pprint(lineup, indent=2)
# return ( lineup )
'''