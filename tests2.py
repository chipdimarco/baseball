# Here is a method for reading the lineup list from a file rather than from online

import json

stats_file = "data/2017_bos_stats.json"
data = json.load(open(stats_file))
'''
player = {}
player["Name"] = data['cumulativeplayerstats']['playerstatsentry'][0]['player']['LastName']
print (player)
'''

#this will throw the exception, but the rest of the numbers will be searched
#home_ids = ['10300','11064','xxxxx','10303', '11339','10301','12551','10297','10296','11065']
#home_ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
home_ids = ['10300']

ids = home_ids
lineup = []

for id in ids:
    for i in range(100):
        try:
            k = data['cumulativeplayerstats']['playerstatsentry'][i]['player']
            if (k["ID"] == id):
                l = data['cumulativeplayerstats']['playerstatsentry'][i]['team']
                m = data['cumulativeplayerstats']['playerstatsentry'][i]['stats']
                player = {**k,**l,**m}
                lineup.append(player)
                #print (player)
                break
        except:
            print(f'error finding {id}')
            break
            
print (lineup)
#



