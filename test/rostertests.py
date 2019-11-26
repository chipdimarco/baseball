import json


#handler = open('data/2017_bos_activeplayers.json','r')
handler = open( 'boxscore.json','r')
data = handler.read()
#data = handler.readlines()
stats=json.loads(data)
boxlines = []
processedids = []
for i in stats:
    if i["ID"] in processedids:
        pass
    else:
        id = i["ID"]
        boxline = {}
        boxline["BO"] = i["BO"]
        boxline["NAME"] = i["NAME"]
        boxline["ID"] = id
        boxline["AB"] = 0
        boxline["H"]  = 0
        boxline["BB"] = 0
        boxline["HR"] = 0
        for j in stats:
            if j["ID"] == id:
                boxline["AB"] += j["AB"]
                boxline["H"]  += j["H"]
                boxline["BB"] += j["BB"]
                boxline["HR"] += j["HR"]
        processedids.append(id)
        boxlines.append(boxline)
handler.close()

print("                 AB   H  BB  HR")
for x in boxlines:
    N  = x["NAME"].ljust(15,' ')
    AB = str(x["AB"]).rjust(4,' ')
    H  = str(x["H"]).rjust(4,' ')
    BB = str(x["BB"]).rjust(4, ' ')
    HR = str(x["HR"]).rjust(4, ' ')
    print (N + AB + H + BB + HR)



#for x in boxlines:
#    print (x)

'''
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