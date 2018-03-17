import tkinter as tk
from tkinter import ttk

screen = tk.Tk()
screen.title("Game Setup")
screen_width=900
screen_height=600
screen.geometry(f'{screen_width}x{screen_height}')
#screen.configure(background="#e8e8e8")
screen.configure(background="blue")

upper_frame = tk.Frame(screen)
upper_frame.grid(column=0,row=0)
upper_frame.grid_columnconfigure(0, minsize = screen_width/3)
upper_frame.grid_columnconfigure(1, minsize = screen_width/3)
upper_frame.grid_columnconfigure(2, minsize = screen_width/3)
upper_frame.grid_rowconfigure(0, minsize = screen_height/5)
upper_frame.config(background="#fff")

text_uf1 = tk.Label(upper_frame,text="This is just a test")
text_uf1.grid(column=1,row=0)

text_uf0 = ttk.Label(upper_frame,text="Left")
text_uf0.grid(column=0,row=0)

text_uf2 = ttk.Label(upper_frame,text="Right")
text_uf2.grid(column=2,row=0)

middle_frame = ttk.Frame(screen)
middle_frame.grid(column=0,row=1)

lower_frame = ttk.Frame(screen)
lower_frame.grid(column=0,row=2)

# Team Selection
options_Teams = ["Red Sox","Yankees", "Blue Jays", "Rays", "Orioles", "Phillies"]
select_VisitingTeam = tk.StringVar(screen)
visitingteamoptions = options_Teams
select_HomeTeam = tk.StringVar(screen)
hometeamoptions = options_Teams
#hometeamoptions = [i for i in options_Teams if i != select_VisitingTeam]
select_VisitingTeam.set ("Visiting Team")
select_HomeTeam.set ("Home Team")

def getVisitingTeam():
    select_VisitingTeam.get()
    print(select_VisitingTeam.get())

def getHomeTeam():
    select_HomeTeam.get()
    print (select_HomeTeam.get())


visitingteam = tk.OptionMenu(lower_frame, select_VisitingTeam, *visitingteamoptions) 
visitingteam.grid(column=0,row=0)

hometeam = tk.OptionMenu(lower_frame, select_HomeTeam, *hometeamoptions) 
hometeam.grid(column=0,row=1)

pickvisitingteam = tk.Button(lower_frame, text="OK", command=getVisitingTeam)
pickvisitingteam.grid(column=1,row=0)

pickhometeam = tk.Button(lower_frame,text="OK", command=getHomeTeam)
pickhometeam.grid(column=1,row=1)