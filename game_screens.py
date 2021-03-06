# 3/17/2018
# 4/20/2018 Refactoring
# help from pythonprogramming.net
# and their YouTube tutorials
#import tkinter as tk
from game_settings import Settings
from game_lineup import Lineup
from game_atbat import Atbat
import game_setup as gs
import json

# Create Objects
settings = Settings()
visitor = Lineup()
home = Lineup()

# Initialize Variables
v_linescore = []
h_linescore = []
LARGE_FONT = ("verdana",14)

"""
# The controller class
class GameScreen(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid(column=0, row=0)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        # creates the Frames (which are the screen/layouts)
        self.frames = {}
        for F in (Splash,Setup,Play):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(Splash)
    # switches among the layout/frames
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


# S P L A S H : FRAME 1 - on open 
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
        splash_label = tk.Label(splash_frame,text="Welcome to Waban Studio Baseball",font=LARGE_FONT, bg="forest green")
        button_setup = tk.Button(splash_frame, text="Go to Setup", width=10, 
            command = lambda: controller.show_frame(Setup))
        button_play = tk.Button(splash_frame, text="Go to Play", width=10,
            command = lambda: controller.show_frame(Play))
        # Place Objects in Frame
        splash_label.grid(column=0,row=0, sticky="nsew", columnspan=2)
        button_setup.grid(column=0,row=1)
        button_play.grid(column=1,row=1)


# S E T U P : FRAME 2: Setup a game - read stats and create roster/lineup 
class Setup(tk.Frame):
    def __init__(self, parent, controller):
        # Create Frame
        tk.Frame.__init__(self, parent)
        setup_frame = tk.Frame(self)
        # Format Frame
        setup_frame.grid(column=0, row=0)
        setup_frame.grid_rowconfigure(0,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(1,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(1,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(2,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(3,minsize=settings.height*.6)
        setup_frame.grid_columnconfigure(0,minsize=settings.width/2)
        setup_frame.grid_columnconfigure(1,minsize=settings.width/2)
        # Create Objects for Frame
        label = tk.Label(setup_frame, text = "Setup", font=LARGE_FONT, bg="forest green")
        button_splash = tk.Button(setup_frame, text="Go to Splash", width=10,
            command = lambda: controller.show_frame(Splash))
        button_play = tk.Button(setup_frame, text="Go to Play", width=10,
            command = lambda: controller.show_frame(Play))
        # Place Objects in Frame
        label.grid(column=0,row=0, sticky="nsew", columnspan=2)
        button_splash.grid(column=0,row=1)
        button_play.grid(column=1,row=1)
        #
        # - - - - - - - - - - - - - - - - - - - - - -
        #Selection Part
        # - - - - - - - - - - - - - - - - - - - - - -
        # Team Selection
        selection_board =tk.Frame(setup_frame)
        selection_board.grid(column=0,row=2, sticky="n")

        # List comprehension will parse out the Keys from this dictionary in Settings
        options_Teams = [i for i in settings.team_codes.keys()]

        # StringVars: they hold the names of the selected teams
        self.select_VisitingTeam = tk.StringVar(selection_board)
        self.select_HomeTeam = tk.StringVar(selection_board)
        #
        visitingteamoptions = options_Teams
        hometeamoptions = options_Teams
        #
        self.select_VisitingTeam.set ("Visiting Team")
        self.select_HomeTeam.set ("Home Team")

        # STRINGVARS: Used with game_setup; they hold the roster information
        self.roster_VisitingTeam = tk.StringVar(selection_board)
        self.roster_HomeTeam = tk.StringVar(selection_board)
        #
        self.setup_result_visitor = tk.StringVar(selection_board)
        self.setup_result_home = tk.StringVar(selection_board)
        #
        self.setup_teamname_visitor = tk.StringVar()
        self.setup_teamname_visitor.set({})
        self.setup_teamname_visitor.set(self.select_VisitingTeam.get())
        #
        self.setup_teamname_home = tk.StringVar()
        self.setup_teamname_home.set({})
        self.setup_teamname_home.set(self.select_HomeTeam.get())
        # 
        # Tkinterface Settings from game_setup
        # Option Menus
        visitingteam = tk.OptionMenu(selection_board, self.select_VisitingTeam, *visitingteamoptions) 
        hometeam     = tk.OptionMenu(selection_board, self.select_HomeTeam    , *hometeamoptions) 
        #
        # The "OK" Buttons
        pickvisitingteam = tk.Button(selection_board, text="OK", command=lambda:  self.setup_result_visitor.set(gs.create_roster_25(self.select_VisitingTeam.get(), self.roster_VisitingTeam,visitor, settings)))
        pickhometeam     = tk.Button(selection_board, text="OK", command=lambda:  self.setup_result_home.set(gs.create_roster_25(self.select_HomeTeam.get(),self.roster_HomeTeam, home, settings)))
        #
        # Display the labels
        visitorlabel = tk.Label(selection_board,textvariable=self.setup_result_visitor)
        homelabel =    tk.Label(selection_board,textvariable=self.setup_result_home)
        #
        # Grid settings

        visitingteam.grid(column=0,row=2, sticky="n", padx=10)
        pickvisitingteam.grid(column=0,row=3, sticky="n",padx=10)
        visitorlabel.grid(column=0,row=4,  sticky="n")
        #
        hometeam.grid(column=1,row=2,  sticky="n")
        pickhometeam.grid(column=1,row=3, sticky="n")
        homelabel.grid(column=1,row=4, sticky="n")
        
    # Setup methods display results from game_setup
    def getVisitorResult(self):
        return(self.setup_result_visitor.get())
    def getHomeResult(self):
        return(self.setup_result_home.get())
    # Setup methods for returning id lists to Play
    def getVisitorTeamname(self):
        return (self.setup_teamname_visitor.get())
    def getHomeTeamname(self):
        return (self.setup_teamname_home.get())


# P L A Y : FRAME 3: Where the game functions take place 
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
        # - - - - - - - - - - - - - - - - - - - - - -
        bleacher_board = tk.Frame(play_frame)
        # Format child frame
        bleacher_board.grid(column=0, row=0, sticky="nsew")
        bleacher_board.grid_rowconfigure(0,minsize=settings.height/10)
        bleacher_board.grid_rowconfigure(1,minsize=settings.height/10)
        bleacher_board.grid_columnconfigure(0,minsize=settings.width/2)
        bleacher_board.grid_columnconfigure(1,minsize=settings.width/2)
        # Create Objects for child frame
        label = tk.Label(bleacher_board, text = "Play Ball!", font=LARGE_FONT, bg="forest green")
        button_splash = tk.Button(bleacher_board, text="Go to Splash", width=10,
            command = lambda: controller.show_frame(Splash))
        button_setup = tk.Button(bleacher_board, text="Go to Setup", width=10,
            command = lambda: controller.show_frame(Setup))

        # Place Objects in Frame
        label.grid(column=0,row=0, sticky="nsew", columnspan=2)
        button_splash.grid(column=0, row=1)
        button_setup.grid(column=1, row=1)
        # - - - - - - - - - - - - - - - - - - - - - -
        # FIELD BOARD - Child Frame (0,1) - Middle Row, 3 Columns
        # - - - - - - - - - - - - - - - - - - - - - -
        # set background color with tk.
        field_board = tk.Frame(play_frame)
        # Format child frame
        field_board.grid_rowconfigure(0,minsize=settings.height/10)
        field_board.grid_rowconfigure(1,minsize=settings.height*.4)
        field_board.grid_columnconfigure(0,minsize=settings.width/4)
        field_board.grid_columnconfigure(1,minsize=settings.width/2)
        field_board.grid_columnconfigure(2,minsize=settings.width/4)
        field_board.grid(column=0, row =1)
        # Create Objects for child frame
        # Place Objects in Frame
        # Display Lineup for Visitors
        visitor_teamname = tk.StringVar()
        button_visitor_teamname = tk.Button(field_board, text="Get Visting Lineup", command = lambda: visitor_teamname.set(visitor.battingorder_result))
        button_visitor_teamname.grid(column=0,row=0, sticky="n")
              
        # Display Lineup for Home
        home_teamname = tk.StringVar()
        button_home_teamname = tk.Button(field_board, text="Get Home Lineup", command = lambda: home_teamname.set(home.battingorder_result))
        button_home_teamname.grid(column=2,row=0, sticky="n")

        # Display Rosters
        v_lineup_card = tk.Label(field_board, textvariable = visitor_teamname)
        v_lineup_card.grid(column= 0, row = 1, sticky="n", padx=12)

        h_lineup_card = tk.Label(field_board, textvariable = home_teamname)
        h_lineup_card.grid(column= 2, row = 1, sticky="n", padx=12)

        # - - - - - - - - - - - - - - - - - - - - - -
        # Field Board > FIELD
        field_height = int(settings.height/3)
        field_width = int(settings.width/3)
        y = int(field_height/4)
        x = int(field_width/4)
        diamond = (2*x,y, 3*x,2*y, 2*x,3*y, x,2*y)
        field = tk.Canvas(field_board,height=field_height,width=field_width)
        field.grid(column=1,row=1, sticky="n")
        field.create_rectangle(0 , 0 , field_width, field_height, fill='#526F35')
        field.create_polygon(diamond, fill=settings.diamond_color)
        # - - - - - - - - - - - - - - - - - - - - - -
        #DUGOUT - Child Frame (0,2) - 3 Columns
        # - - - - - - - - - - - - - - - - - - - - - -
        dugout = tk.Frame(play_frame)
        dugout.grid(column=0, row=2, sticky="n")
        dugout.grid_rowconfigure(0,minsize=settings.height*.3)
        dugout.grid_columnconfigure(0,minsize=settings.width/4)
        dugout.grid_columnconfigure(1,minsize=settings.width/4)
        dugout.grid_columnconfigure(2,minsize=settings.width/2)


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
        h_linescore.grid(column=1,row=2,sticky=("nw"))

        # Dugout > PLAY BY PLAY
        # the atbat.inning_top method will also set the play_by_play StringVar, and the message object below will draw it on screen
        message = tk.Label(dugout,textvariable=atbat.play_by_play)
        message.grid(column=2,row=0,sticky=("nw"))
"""
