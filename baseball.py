# -----------------v2---------------------------
# Use the MySportsFeeds API to retrieve MLB info
# 10/20/2019: new version for clibaseball
# 11/02/2019: Box class
# 11/03/2019: Game class
# -----------------v1---------------------------
# 3/18/2018: Move Tkinter screen creation to game_screens module

# IMPORT
import sys

import game as g

#   V A R I A B L E S
stadium_name = "Waban Field"
PLAY_BY_PLAY = False
YEAR         = 2018

#   M A I N   F U N C T I O N
def main():
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

if __name__ == "__main__":
    main()
