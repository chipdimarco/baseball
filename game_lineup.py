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
        self.lineup_dictionary = ""
        self.lineup_lastname = ""
        self.pitcher = ""
    
    def getInfo(self,id):
        self.id = id
        qs = {}
        qs["player"]=id
        return (requests.get(url,headers=headers,params=qs).json())


    # Method for creating a lineup with stats from a dict. of ids
    def create_lineup_dictionary(self,ids):
        self.ids = ids

        # Init lineup as dictionary
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
            j['batterstrikeouts']=r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['BatterStrikeouts']['#text']
            j['battergroundouts']=r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['BatterGroundOuts']['#text']
            j['batterflyouts']=r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['BatterFlyOuts']['#text']
            lineup.append(j)
        # return the lineup
        return (lineup)

    def create_lineup_lastname(self, lineup_dictionary):
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
        j['pitchergroundouts'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['PitcherGroundOuts']['#text']
        j['pitcherflyouts'] = r['cumulativeplayerstats']['playerstatsentry'][0]['stats']['PitcherFlyOuts']['#text']
        
        return (j)


