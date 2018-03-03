import json


handler = open('data/2017_bos_activeplayers.json','r')
data = handler.read()
stats=json.loads(data)
handler.close()

length = len(stats["activeplayers"]["playerentry"])
#result = stats["activeplayers"]["playerentry"][0]["player"]["LastName"]
#print (length)
roster = []
for i in range (length):
    player = {}
    player["ID"]= stats["activeplayers"]["playerentry"][i]["player"]["ID"]
    #player["FirstName"]= stats["activeplayers"]["playerentry"][i]["player"]["FirstName"]
    #player["LastName"]= stats["activeplayers"]["playerentry"][i]["player"]["LastName"]
    player["Name"]= (f'{stats["activeplayers"]["playerentry"][i]["player"]["FirstName"]} {stats["activeplayers"]["playerentry"][i]["player"]["LastName"]}')
    player["Position"]= stats["activeplayers"]["playerentry"][i]["player"]["Position"]
    roster.append(player)
print(roster)


'''
handler = open('data/2017_bos_stats.json','r')
data = handler.read()
stats=json.loads(data)
handler.close()

#result = stats["cumulativeplayerstats"]["playerstatsentry"][0]["player"]
length = len(stats["cumulativeplayerstats"]["playerstatsentry"])

for i in range (length):
    player = {}
    player["ID"] = stats["cumulativeplayerstats"]["playerstatsentry"][i]["player"]["ID"]
    player["FirstName"] = stats["cumulativeplayerstats"]["playerstatsentry"][i]["player"]["FirstName"]
    player["LastName"] = stats["cumulativeplayerstats"]["playerstatsentry"][i]["player"]["LastName"]
    player["GamesPlayed"] = stats["cumulativeplayerstats"]["playerstatsentry"][i]["stats"]["GamesPlayed"]["#text"]
    player["GamesStarted"] = stats["cumulativeplayerstats"]["playerstatsentry"][i]["stats"]["GamesStarted"]["#text"]
    player["RangeFactor"] = stats["cumulativeplayerstats"]["playerstatsentry"][i]["stats"]["RangeFactor"]["@abbreviation"]
    #print(stats["cumulativeplayerstats"]["playerstatsentry"][i]["player"]["ID"])
    print (player)

#print (result)
'''