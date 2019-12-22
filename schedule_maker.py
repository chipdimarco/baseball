# 11-21-2019
# v1 for a basic scheduler, which is a set of
# loops through a list of teams that creates
# a list of home/away matchups for a 3-game 
# series.
#
# This version creates a 156-game season for
# 30 AL teams in 3 divisions


# List of Teams
league = [
    {
        "Div":"ALE",
        "Teams": ["BOS", "NYY", "TB", "TOR", "BAL"]
    },
    {
        "Div": "ALC",
        "Teams": ["CLE", "MIN", "CWS", "DET", "KC"]
    },
    {
        "Div": "ALW",
        "Teams": ["TEX", "HOU", "SEA", "LAA", "OAK"]
    }
]

def generate_schedule():
    # return SCHEDULE
    SCHEDULE = []
    GAME_NUMBER = 1
    # games_per_series - default is 3
    gps = 3
    # times one team hosts a series with another team
    # default 4
    home_series_indiv = 4
    # default 1
    home_series_outdiv = 1
    # default is 3x4x4  = 48 vs div
    #            3x1x10 = 30 vs non-div
    #                   = 78 x 2 = 156 
    for div in league:
        #print (div["Div"])
        for team in div["Teams"]:
            for opp in div["Teams"]:
                for series in range( home_series_indiv):
                    if team != opp:
                        x = {}
                        x['home'] = team
                        x['visitor'] = opp
                        x['series']  = gps
                        x['game_number'] = GAME_NUMBER
                        SCHEDULE.append(x)
                        GAME_NUMBER += 1
            for outdiv in league:
                if outdiv["Div"] != div["Div"]:
                    for opp in outdiv["Teams"]:
                        for series in range ( home_series_outdiv ):
                            if team != opp:
                                x = {}
                                x['home'] = team
                                x['visitor'] = opp
                                x['series']  = gps
                                x['game_number'] = GAME_NUMBER
                                SCHEDULE.append(x)
                                GAME_NUMBER += 1
    return ( SCHEDULE )


    # 11-21-2019 to put standings together

def print_standings( RESULTS ):
    PLAY_BY_PLAY = False
    STANDINGS = {}
    # replace hard coded teams with teams in league
    STANDINGS["MIN"] = {"W":0,"L":0,"T":0}
    STANDINGS["CLE"] = {"W":0,"L":0,"T":0}
    STANDINGS["CWS"] = {"W":0,"L":0,"T":0}
    STANDINGS["DET"] = {"W":0,"L":0,"T":0}
    STANDINGS["KC"] = {"W":0,"L":0,"T":0}
    STANDINGS["BOS"] = {"W":0,"L":0,"T":0}
    STANDINGS["NYY"] = {"W":0,"L":0,"T":0}
    STANDINGS["BAL"] = {"W":0,"L":0,"T":0}
    STANDINGS["TOR"] = {"W":0,"L":0,"T":0}
    STANDINGS["TB"] = {"W":0,"L":0,"T":0}
    STANDINGS["OAK"] = {"W":0,"L":0,"T":0}
    STANDINGS["SEA"] = {"W":0,"L":0,"T":0}
    STANDINGS["TEX"] = {"W":0,"L":0,"T":0}
    STANDINGS["HOU"] = {"W":0,"L":0,"T":0}
    STANDINGS["LAA"] = {"W":0,"L":0,"T":0}

    if PLAY_BY_PLAY: 
        print (f'RESULTS')
    for r in RESULTS:
        visitor = r[0]
        v_score = r[1]
        home    = r[2]
        h_score = r[3]
        if h_score > v_score:
            if PLAY_BY_PLAY:
                print (f'{home} beats {visitor}, {h_score}-{v_score}')
            STANDINGS[home]["W"] += 1
            STANDINGS[visitor]["L"] += 1
        elif v_score > h_score:
            if PLAY_BY_PLAY:
                print (f'{ visitor } beats { home }, {v_score}-{h_score}')
            STANDINGS[visitor]["W"] += 1
            STANDINGS[home]["L"] += 1
        else:
            if PLAY_BY_PLAY:
                print (f'{visitor} and {home} tied, {v_score}-{h_score}')
            STANDINGS[visitor]["T"] += 1
            STANDINGS[home]["T"] += 1
    print (f'\nSTANDINGS')
    for k,v in STANDINGS.items():
        print(k,f'{v["W"]} {v["L"]} {v["T"]}')
    



def main():
#    print ("Hello World")
    s = generate_schedule()
    for y in s:
        print (f'{ y["home"] } hosts {y["visitor"]} for {y["series"]} games')

if __name__ == "__main__":
    main()

#exit()
