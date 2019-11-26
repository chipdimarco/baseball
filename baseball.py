# -----------------v2---------------------------
# Use the MySportsFeeds API to retrieve MLB info
# 10/20/2019: new version for clibaseball
#   - 11/02/2019: Box class
#   - 11/03/2019: Game class
#   - 11/21/2019: Plays a 156-game schedule for a 30 team league
#     and output is a W-L-T list of standings. 
# -----------------v1---------------------------
# 3/18/2018: Move Tkinter screen creation to game_screens module

#   I M P O R T
import sys
import game as g
import schedule_maker as sm


#   V A R I A B L E S
PLAY_BY_PLAY = False
YEAR         = 2019
RESULTS      = []

#   F U N C T I O N S
def play_one_game():
    print(f"\nPLAY BALL!\n==========")
    game = g.Game()
    game.get_game_input()
    game.get_game_objects()
    if PLAY_BY_PLAY:
        print (f'\nThe matchup: {game.visiting_team_name} at {game.home_team_name}\n')    
        game.print_roster_info()
    game.play_game()
    game.postgame()
    print (f"GAME OVER!\n==========\n")

def play_scheduled_game(matchup):
    if PLAY_BY_PLAY:
        print(f"\nPLAY BALL!\n==========")
    v = matchup["visitor"]
    h = matchup["home"]
    game = g.Game()
    game.set_scheduled_game_input(v,h)
    game.get_game_objects()
    if PLAY_BY_PLAY:
        print (f'\nThe matchup: {game.visiting_team_name} at {game.home_team_name}\n')    
        game.print_roster_info()
    game.play_game()
    result = game.postgame()
    if PLAY_BY_PLAY:
        print (f"GAME OVER!\n==========\n")
    return (result)

#   M A I N   F U N C T I O N
def main():
    option = input("\nChoose a play option:\n  [1] One off\n  [2] Schedule\n  ")
    if option == "1":
        play_one_game()
        exit()
    elif option == "2":
        SCHEDULE = sm.generate_schedule()
        for matchup in SCHEDULE:
            for i in range(matchup["series"]):
                result = play_scheduled_game( matchup )
                RESULTS.append(result)
    else:
        print ("input error")
        exit
    # 11-21-2019 to put standings together
    STANDINGS = {}
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

if __name__ == "__main__":
    main()

'''   
    print(f"\nPLAY BALL!\n==========")
    game = g.Game()
    game.get_game_input()
    game.get_game_objects()
    if PLAY_BY_PLAY:
        print (f'\nThe matchup: {game.visiting_team_name} at {game.home_team_name}\n')    
        game.print_roster_info()
    game.play_game()
    game.postgame()
    print (f"GAME OVER!\n==========\n")
'''

'''
    # 11-18-2019 to put standings together
    STANDINGS = {}
    STANDINGS["MIN"] = 0
    STANDINGS["CLE"] = 0
    STANDINGS["CWS"] = 0
    STANDINGS["DET"] = 0
    STANDINGS["KC"] = 0
    STANDINGS["BOS"] = 0
    STANDINGS["NYY"] = 0
    STANDINGS["BAL"] = 0
    STANDINGS["TOR"] = 0
    STANDINGS["TB"] = 0
    STANDINGS["OAK"] = 0
    STANDINGS["SEA"] = 0
    STANDINGS["TEX"] = 0
    STANDINGS["HOU"] = 0
    STANDINGS["LAA"] = 0

'''

