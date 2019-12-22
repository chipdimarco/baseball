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
from game_settings import Settings


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
    #
    game.game_number = matchup["game_number"]
    #
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
#        print ("input error")
        play_one_game()
        exit()
    elif option == "2":
#        print ("input error")
        SCHEDULE = sm.generate_schedule()
        for matchup in SCHEDULE:
            for i in range(matchup["series"]):
                result = play_scheduled_game( matchup )
                RESULTS.append(result)
        sm.print_standings(RESULTS)
    else:
        print ("input error")
        exit()
    exit()

if __name__ == "__main__":
    main()
