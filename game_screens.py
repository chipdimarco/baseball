# 3/17/2018
# help from pythonprogramming.net
import tkinter as tk
from game_settings import Settings
from game_lineup import Lineup

settings = Settings()

LARGE_FONT = ("verdana",14)
home_team_name = "Red Sox"
visiting_team_name = "Yankees"

visitor = Lineup()
visitor_pitcher_id ="10719"
visitor_ids =['10728','10729','10440','11091','10730','11092','11293','10734','10726']
visitor_stats_file = "data/2017_nyy_stats.json"

visitor.lineup_dictionary = visitor.create_lineup_dictionary_from_file(visitor_stats_file,visitor_ids)
visitor.lineup_lastname = visitor.create_lineup_lastname(visitor.lineup_dictionary) 
visitor.pitcher = visitor.get_pitcher_from_file(visitor_stats_file, visitor_pitcher_id)

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


class Splash(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        splash_frame = tk.Frame(self)
        splash_frame.grid(column=0,row=0)
        splash_frame.grid_rowconfigure(0,minsize=settings.height/10)
        splash_frame.grid_rowconfigure(1,minsize=settings.height/10)
        splash_frame.grid_rowconfigure(2,minsize=settings.height*.8)
        splash_frame.grid_columnconfigure(0,minsize=settings.width/2)
        splash_frame.grid_columnconfigure(1,minsize=settings.width/2)

        splash_label = tk.Label(splash_frame,text="Welcome to Waban Studio Baseball",font=LARGE_FONT)
        button_setup = tk.Button(splash_frame, text="Go to Setup", width=10, 
            command = lambda: controller.show_frame(Setup))
        button_play = tk.Button(splash_frame, text="Go to Play", width=10,
            command = lambda: controller.show_frame(Play))

        splash_label.grid(column=0,row=0, sticky="n", columnspan=2)
        button_setup.grid(column=0,row=1, sticky="n")
        button_play.grid(column=1,row=1,sticky="n")


class Setup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        setup_frame = tk.Frame(self)
        setup_frame.grid(column=0, row=0)
        setup_frame.grid_rowconfigure(0,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(1,minsize=settings.height/10)
        setup_frame.grid_rowconfigure(2,minsize=settings.height*.8)
        setup_frame.grid_columnconfigure(0,minsize=settings.width/2)
        setup_frame.grid_columnconfigure(1,minsize=settings.width/2)

        label = tk.Label(setup_frame, text = "Setup", font=LARGE_FONT)
        button_splash = tk.Button(setup_frame, text="Go to Splash", width=10,
            command = lambda: controller.show_frame(Splash))
        button_play = tk.Button(setup_frame, text="Go to Play", width=10,
            command = lambda: controller.show_frame(Play))
        
        label.grid(column=0,row=0, sticky="n", columnspan=2)
        button_splash.grid(column=0,row=1,sticky="n")
        button_play.grid(column=1,row=1, sticky="n")





class Play(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        play_frame = tk.Frame(self)
        play_frame.grid(column=0,row=0)

        #BLEACHER BOARD - Frame (0,0) - Top Row
        bleacher_board = tk.Frame(play_frame)
        bleacher_board.grid(column=0, row=0)
        bleacher_board.grid_rowconfigure(0,minsize=settings.height/10)
        bleacher_board.grid_columnconfigure(0,minsize=settings.width/2)

        label = tk.Label(bleacher_board, text = "Play Ball!", font=LARGE_FONT)
        button_splash = tk.Button(bleacher_board, text="Go to Splash", width=10,
            command = lambda: controller.show_frame(Splash))
        button_setup = tk.Button(bleacher_board, text="Go to Setup", width=10,
            command = lambda: controller.show_frame(Setup))

        label.grid(column=0,row=0, sticky="n", columnspan=2)
        button_splash.grid(column=0,row=1,sticky="w")
        button_setup.grid(column=1,row=1,sticky="w")

        # FIELD BOARD - Frame (0,1) - Middle Row, 3 Columns
        field_board = tk.Frame(play_frame)
        field_board.grid_columnconfigure(0,minsize=settings.width/4)
        field_board.grid_columnconfigure(1,minsize=settings.width/2)
        field_board.grid_columnconfigure(2,minsize=settings.width/4)
        field_board.grid_rowconfigure(0,minsize=settings.height/2)
        field_board.grid(column=0, row =1)


        #DUGOUT - Frame (0,2) - 3 Columns
        dugout = tk.Frame(play_frame)
        dugout.grid(column=0, row=2)
        dugout.grid_columnconfigure(0,minsize=settings.width/4)
        dugout.grid_columnconfigure(1,minsize=settings.width/4)
        dugout.grid_columnconfigure(2,minsize=settings.width/2)
        dugout.grid_rowconfigure(0,minsize=settings.height*.4)

        # Field Board > LINEUP CARDS
        viz = (f'VISITORS\n\n{visiting_team_name}\n')
        vlc=tk.StringVar()
        vlc.set(viz)
        
        for i in visitor.lineup_lastname:
            viz += (f'\n{i}')
        
        vlc=tk.StringVar()
        vlc.set(viz)

        v_lineup_card = tk.Label(field_board, textvariable = vlc)
        v_lineup_card.grid(column = 0, row = 0, sticky="n")


        '''
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
        v_lineup_card.grid(column= 0, row = 0, sticky="n", padx=12)

        hlc=tk.StringVar()
        hlc.set(hiz)
        h_lineup_card = tk.Label(field_board, textvariable = hlc)
        h_lineup_card.grid(column= 2, row = 0, sticky="n", padx=12)
        
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
        '''






'''
# call this from baseball.py
app = GameScreen()
app.mainloop()
'''