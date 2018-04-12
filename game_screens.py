# 3/17/2018
# help from pythonprogramming.net
# and their YouTube tutorials
import tkinter as tk
from game_settings import Settings
from game_lineup import Lineup
from game_atbat import Atbat
import game_setup as gs


settings = Settings()
v_linescore = []
h_linescore = []

LARGE_FONT = ("verdana",14)

# Visitor Setup
visiting_team_name = "Yankees"

visitor = Lineup()
visitor_pitcher_id ="10719"
visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
visitor_stats_file = "data/2017_nyy_stats.json"

visitor.lineup_dictionary = visitor.create_lineup_dictionary_from_file(visitor_stats_file,visitor_ids)
visitor.lineup_lastname = visitor.create_lineup_lastname(visitor.lineup_dictionary) 
visitor.pitcher = visitor.get_pitcher_from_file(visitor_stats_file, visitor_pitcher_id)

# Home Setup
home_team_name = "Red Sox"

home = Lineup()
home_pitcher_id = "10432"
home_ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
home_stats_file = "data/2017_bos_stats.json"
    
home.lineup_dictionary = home.create_lineup_dictionary_from_file(home_stats_file,home_ids)
home.lineup_lastname = home.create_lineup_lastname(home.lineup_dictionary)
home.pitcher = home.get_pitcher_from_file(home_stats_file, home_pitcher_id)


class GameScreen(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(column=0, row=0)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        for F in (Splash,Setup,Play):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(Splash)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_something(self,cont):
        frame = self.frames[cont]
        something = frame.getHomeRoster()
        #print (something)
        return(something)


class Splash(tk.Frame):
    def __init__(self,parent,controller):
        # Create Frame
        tk.Frame.__init__(self,parent)
        splash_frame = tk.Frame(self)
        # Format Frame
        splash_frame.grid(column=0,row=0)
        splash_frame.grid_rowconfigure(0,minsize=settings.height/10)
        splash_frame.grid_rowconfigure(1,minsize=settings.height/10)
        splash_frame.grid_rowconfigure(2,minsize=settings.height*.8)
        splash_frame.grid_columnconfigure(0,minsize=settings.width/2)
        splash_frame.grid_columnconfigure(1,minsize=settings.width/2)
        # Create Objects for Frame
        splash_label = tk.Label(splash_frame,text="Welcome to Waban Studio Baseball",font=LARGE_FONT)
        button_setup = tk.Button(splash_frame, text="Go to Setup", width=10, 
            command = lambda: controller.show_frame(Setup))
        button_play = tk.Button(splash_frame, text="Go to Play", width=10,
            command = lambda: controller.show_frame(Play))
        # Place Objects in Frame
        splash_label.grid(column=0,row=0, sticky="n", columnspan=2)
        button_setup.grid(column=0,row=1, sticky="n")
        button_play.grid(column=1,row=1,sticky="n")


class Setup(tk.Frame):
    def __init__(self, parent, controller):
        # Create Frame
        tk.Frame.__init__(self, parent)
        setup_frame = tk.Frame(self)
        # Format Frame
        setup_frame.grid(column=0, row=0)
        setup_frame.grid_rowconfigure(0,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(1,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(2,minsize=settings.height*.8)
        setup_frame.grid_columnconfigure(0,minsize=settings.width/2)
        setup_frame.grid_columnconfigure(1,minsize=settings.width/2)
        # Create Objects for Frame
        label = tk.Label(setup_frame, text = "Setup", font=LARGE_FONT)
        button_splash = tk.Button(setup_frame, text="Go to Splash", width=10,
            command = lambda: controller.show_frame(Splash))
        button_play = tk.Button(setup_frame, text="Go to Play", width=10,
            command = lambda: controller.show_frame(Play))
        # Place Objects in Frame
        label.grid(column=0,row=0, sticky="n", columnspan=2)
        button_splash.grid(column=0,row=1,sticky="n")
        button_play.grid(column=1,row=1, sticky="n")
        #
        #Selection Part
        # Team Selection
        selection_board =tk.Frame(setup_frame)
        selection_board.grid(column=0,row=2)

        # List comprehension will parse out the Keys from this dictionary in Settings
        # options_Teams = ["Red Sox","Yankees", "Blue Jays", "Rays", "Orioles", "Phillies"] # old way
        options_Teams = [i for i in settings.team_codes.keys()]

        select_VisitingTeam = tk.StringVar(selection_board)
        visitingteamoptions = options_Teams
        select_HomeTeam = tk.StringVar(selection_board)
        hometeamoptions = options_Teams
        #hometeamoptions = [i for i in options_Teams if i != select_VisitingTeam]
        select_VisitingTeam.set ("Visiting Team")
        select_HomeTeam.set ("Home Team")

        # Used with game_setup
        self.roster_VisitingTeam = tk.StringVar(selection_board)
        self.roster_HomeTeam = tk.StringVar(selection_board)
        # Tkinterface Settings from game_setup
        # Option Menus
        visitingteam = tk.OptionMenu(selection_board, select_VisitingTeam, *visitingteamoptions) 
        hometeam = tk.OptionMenu(selection_board, select_HomeTeam, *hometeamoptions) 

        # Buttons
        pickvisitingteam = tk.Button(selection_board, text="OK", command=lambda: gs.create_roster_25(select_VisitingTeam.get
        (), self.roster_VisitingTeam))
        pickhometeam = tk.Button(selection_board,text="OK", command= lambda: gs.create_roster_25(select_HomeTeam.get(),self.roster_HomeTeam))

        # Display Labels
        visitorlabel = tk.Label(selection_board,textvariable=self.roster_VisitingTeam)
        homelabel = tk.Label(selection_board,textvariable=self.roster_HomeTeam)

        # Grid settings
        visitingteam.grid(column=0,row=0)
        pickvisitingteam.grid(column=1,row=0)
        #visitorlabel.grid(column=0,row=1)
        visitorlabel.grid(column=0,row=1)

        hometeam.grid(column=2,row=0)
        pickhometeam.grid(column=3,row=0)
        homelabel.grid(column=2,row=1)
        # homelabel.grid(column=2,row=1)

    def getVisitingTeam(self):
        result = select_VisitingTeam.get()
        #print(select_VisitingTeam.get())
        print ( result )
        return ( result )

    def getHomeTeam(self):
        select_HomeTeam.get()
        print (select_HomeTeam.get())

    def getHomeRoster(self):
        print(self.roster_HomeTeam.get())
        return(self.roster_HomeTeam.get())
        # return ("something in getHomeRoster")
        '''
        '''
    





class Play(tk.Frame):
    def __init__(self, parent, controller):
        # Create Frame
        tk.Frame.__init__(self, parent)
        # Format Frame
        play_frame = tk.Frame(self)
        play_frame.grid(column=0,row=0)
        # Create atbat object
        atbat = Atbat()
        # - - - - - - - - - - - - - - - - - - - - - -
        # Create Child Frames
        # - - - - - - - - - - - - - - - - - - - - - -
        #BLEACHER BOARD - Child Frame (0,0) - Top Row
        bleacher_board = tk.Frame(play_frame)
        # Format child frame
        bleacher_board.grid(column=0, row=0)
        bleacher_board.grid_rowconfigure(0,minsize=settings.height/10)
        bleacher_board.grid_columnconfigure(0,minsize=settings.width/2)
        # Create Objects for child frame
        label = tk.Label(bleacher_board, text = "Play Ball!", font=LARGE_FONT)
        button_splash = tk.Button(bleacher_board, text="Go to Splash", width=10,
            command = lambda: controller.show_frame(Splash))
        button_setup = tk.Button(bleacher_board, text="Go to Setup", width=10,
            command = lambda: controller.show_frame(Setup))

        ###########
        # 4-3-2018: This works
        # v_roster = gs.Roster()
        # print (v_roster.note)
        # v_roster_label = tk.Label(bleacher_board, text= v_roster.note)
        # v_roster_label.grid(column=1,row=0, sticky="n")
        
        ###########
        # 4-9-2018 This works
        # something = tk.StringVar()
        # something.set("something string var")
        # v_roster_label = tk.Label(bleacher_board, textvariable=something)
        # v_roster_label.grid(column=1,row=0, sticky="n")
        
        ###########
        #4-11-2018
        something = tk.StringVar()
        # something.set(controller.get_something(Setup))
        #print(something.set(controller.get_something(Setup)))
        button_something = tk.Button(bleacher_board, text="Get Something",
            command = lambda: something.set(controller.get_something(Setup)))
        button_something.grid(column=1,row=0, sticky="n")
        
        
        # Place Objects in Frame
        label.grid(column=0,row=0, sticky="n", columnspan=2)
        button_splash.grid(column=0,row=1,sticky="w")
        button_setup.grid(column=1,row=1,sticky="w")
        # - - - - - - - - - - - - - - - - - - - - - -
        # FIELD BOARD - Child Frame (0,1) - Middle Row, 3 Columns
        field_board = tk.Frame(play_frame)
        # Format child frame
        field_board.grid_columnconfigure(0,minsize=settings.width/4)
        field_board.grid_columnconfigure(1,minsize=settings.width/2)
        field_board.grid_columnconfigure(2,minsize=settings.width/4)
        field_board.grid_rowconfigure(0,minsize=settings.height/2)
        field_board.grid(column=0, row =1)
        # Create Objects for child frame
        # Place Objects in Frame
        # - - - - - - - - - - - - - - - - - - - - - -
        #DUGOUT - Child Frame (0,2) - 3 Columns
        dugout = tk.Frame(play_frame)
        dugout.grid(column=0, row=2)
        dugout.grid_columnconfigure(0,minsize=settings.width/4)
        dugout.grid_columnconfigure(1,minsize=settings.width/4)
        dugout.grid_columnconfigure(2,minsize=settings.width/2)
        dugout.grid_rowconfigure(0,minsize=settings.height*.4)

        # - - - - - - - - - - - - - - - - - - - - - -
        # Create objects in the Child Frames
        # - - - - - - - - - - - - - - - - - - - - - -
        # Field Board > LINEUP CARDS
        viz = (f'VISITORS\n\n{visiting_team_name}\n')
        for i in visitor.lineup_lastname:
            viz += (f'\n{i}')
        hiz = (f'HOME\n\n{home_team_name}\n')
        for i in home.lineup_lastname:
            hiz += (f'\n{i}')
        
        vlc=tk.StringVar()
        vlc.set(viz)
        v_lineup_card = tk.Label(field_board, textvariable = vlc)
        # v_lineup_card = tk.Label(field_board, textvariable = something)
        v_lineup_card.grid(column= 0, row = 0, sticky="n", padx=12)

        hlc=tk.StringVar()
        hlc.set(hiz)
        # h_lineup_card = tk.Label(field_board, textvariable = hlc)
        h_lineup_card = tk.Label(field_board, textvariable = something)
        h_lineup_card.grid(column= 2, row = 0, sticky="n", padx=12)
        
        # - - - - - - - - - - - - - - - - - - - - - -
        # Field Board > FIELD
        field_height = int(settings.height/2)
        field_width = int(settings.width/2)
        y = int(field_height/4)
        x = int(field_width/4)
        diamond = (2*x,y, 3*x,2*y, 2*x,3*y, x,2*y)
        field = tk.Canvas(field_board,height=field_height,width=field_width)
        field.grid(column=1,row=0)
        field.create_rectangle(0 , 0 , field_width, field_height, fill='#526F35')
        field.create_polygon(diamond, fill=settings.diamond_color)

        # - - - - - - - - - - - - - - - - - - - - - -
        # Dugout > PLAY Button
        playNextHalfInningButton = tk.Button( dugout, text="PLAY", command=lambda: atbat.half_inning(settings, visitor, home))
        playNextHalfInningButton.grid(column=0,row=0, sticky="n", padx=24,pady=24)
        
        # - - - - - - - - - - - - - - - - - - - - - -
        # Dugout > LINESCORE_FRAME        
        linescore_frame = tk.Frame(dugout)
        linescore_frame.grid(column=1,row=0,sticky="n")

        # Row 0 is Text
        v = tk.StringVar()
        tk.Label(linescore_frame,textvariable=v).grid(column=1,row=0, sticky = ("nw"))
        v.set("It's a great day for baseball")
        # Row 1 is Visitors Linescore
        v_linescore = tk.Label(linescore_frame, textvariable=atbat.v_linescore)
        v_linescore.grid(column=1,row=1,sticky=("nw"))
        # Row 2 is Home Linescore
        h_linescore = tk.Label(linescore_frame, textvariable=atbat.h_linescore)
        #h_linescore = tk.Label(linescore_frame, text="atbat wont work")
        h_linescore.grid(column=1,row=2,sticky=("nw"))

        # Dugout > PLAY BY PLAY
        # the atbat.inning_top method will also set the play_by_play StringVar, and the message object below will draw it on screen
        message = tk.Label(dugout,textvariable=atbat.play_by_play)
        #message = tk.Label(dugout,text="atbat.play_by_play")
        message.grid(column=2,row=0,sticky=("nw"))

