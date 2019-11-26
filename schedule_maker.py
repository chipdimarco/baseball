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
    # games_per_series - default is 3
    gps = 1
    # times one team hosts a series with another team
    home_series_indiv = 1
    home_series_outdiv = 0
    for div in league:
        #print (div["Div"])
        for team in div["Teams"]:
            for opp in div["Teams"]:
                for series in range( home_series_indiv):
#                    for game in range (gps):
                    if team != opp:
                        x = {}
                        x['home'] = team
                        x['visitor'] = opp
                        x['series']  = gps
                        SCHEDULE.append(x)
            for outdiv in league:
                if outdiv["Div"] != div["Div"]:
                    for opp in outdiv["Teams"]:
                        for series in range ( home_series_outdiv ):
                            if team != opp:
                                x = {}
                                x['home'] = team
                                x['visitor'] = opp
                                x['series']  = gps
                                SCHEDULE.append(x)
    return ( SCHEDULE )

def main():
#    print ("Hello World")
    s = generate_schedule()
    for y in s:
        print (f'{ y["home"] } hosts {y["visitor"]} for {y["series"]} games')

if __name__ == "__main__":
    main()

#exit()
