# Use the MySportsFeeds API to retrieve MLB info
# 2/11/2018 v7: Refactor for putting the game play into the atbat class AND to use Tkinter, not pygame, for interface
# 2/4/2018 v5: Use Atbat() to get results and begin creating a loop through a lineup
# 2/3/2018 v4: Add pygame files for functions, score, setting

# IMPORT
#import requests
#import json
# also import
from game_lineup import Lineup
from game_atbat import Atbat
from tkinter import *
from tkinter import ttk
from game_settings import Settings
from game_score import Score
import sys

import game_functions as gf

# Game functions
def main():
    home_team_name = "Red Sox"
    visiting_team_name = "Yankees"
    # Create a roster for each team
    # Select the lineup. There will be a string of ids for each lineup.
    home_ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
    visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
   
    # Create Lineups
    home = Lineup()
    '''
    home_lineup_dictionary = home.create_lineup_dictionary(home_ids)
    home_lineup_lastname = home.lineup_lastname(home_lineup_dictionary)
    '''

    # Confirm
    # print (home_lineup_lastname)
    visitor = Lineup()
    visitor_lineup_dictionary = visitor.create_lineup_dictionary(visitor_ids)
    visitor_lineup_lastname = visitor.lineup_lastname(visitor_lineup_dictionary) 
    # Confirm
    #print (visitor_lineup_lastname)
     #
    # And Select a pitcher for each team
    home_pitcher_id = ['10432']
    home_pitcher = home.get_pitcher(home_pitcher_id)
    '''
    visitor_pitcher_id =['10719']
    visitor_pitcher = visitor.get_pitcher(visitor_pitcher_id)
    '''
    #print (f'{home_pitcher["lastname"]} is the starting pitcher for the {home_team_name}')
    #print (f'And {visitor_pitcher["lastname"]} will start for the {visiting_team_name}')

    #print (f'{home_pitcher["lastname"]} allowed {home_pitcher["homerunsallowed"]} homeruns last year.')
    
    # Access Game Score
    score = Score()
    #score.v_score = 0
    #score.h_score = 0

    #v6 Loop 9 times
    atbat = Atbat()
    inning = 1
    visitor_leads_off_inning = 0
    home_leads_off_inning = 0
    

    


    # def inning_top (self, inning, visitor_lineup_dictionary, visitor_leads_off_inning, home_pitcher )
    #inning_top = atbat.inning_top(inning, visitor_lineup_dictionary, visitor_leads_off_inning, home_pitcher)
    '''
    print ( inning_top )
    score.v_score += inning_top["v_score"]
    visitor_leads_off_inning = inning_top["visitor_leads_off_inning"]
    '''
    #print (f'Game Over')
    #print (f'Visitor Hits: {score.v_score}  Home Hits: {score.h_score}')


    # Access Game Settings
    settings = Settings()
    screen = Tk()
    screen.title(settings.caption)

    #this should be a method in Settings, yes?
    mainframe = ttk.Frame(screen, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N,W,S,E))
    mainframe.columnconfigure(0,weight=1)
    mainframe.columnconfigure(1,weight=1)
    mainframe.columnconfigure(2,weight=1)
    mainframe.rowconfigure(0,weight=1)

    ttk.Label(mainframe,text=visiting_team_name).grid(column=0,row=0,sticky=W)
    ttk.Label(mainframe,text=home_team_name).grid(column=2, row =0, sticky=E)
    
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5,pady=5)

    field_height = 400
    field_width = 600
    y = int(field_height/4)
    x = int(field_width/4)
    diamond = (2*x,y, 3*x,2*y, 2*x,3*y, x,2*y)
    field = Canvas(screen,height=field_height,width=field_width)
    field.grid(column=0,row=1,sticky=(W,E))
    #field.create_line(0,y,field_width,y,fill="#476042")

    field.create_rectangle(0 , 0 , field_width, field_height, fill='green')
    field.create_polygon(diamond, fill=settings.diamond_color)

    dugout = ttk.Frame(screen,padding="3 3 3 12")
    dugout.grid(column=0, row=2)
    ttk.Label(dugout,text="Welcome to Home Field").grid(column=1,row=0, sticky=N)

    #quitButton = ttk.Button(dugout, text="Quit", command=gf.doSomething).grid(column=0,row=0,sticky=W)
    playButton = ttk.Button(dugout, text="Play", command=lambda: atbat.inning_top(inning, visitor_lineup_dictionary, visitor_leads_off_inning, home_pitcher)).grid(column=0,row=0)
    #playButton = ttk.Button(dugout, text="Play")
    
    #dugout.columnconfigure(0,weight=1)
    #dugout.rowconfigure(0,weight=1)
    #field.pack()
    #field.grid()


    #screen.mainloop()


    # Loop until the user is done
    #done = True
    done = False
    

    
    # ------- M A I N   P R O G R A M   L O O P ------- #
    while not done:
        screen.mainloop()


if __name__ == "__main__":
    main()

