import tkinter as tk
from tkinter import ttk
'''
#from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter.ttk import *
'''
# function that takes the value and updates it with set
def updatemessage(s):
    s.set ("Update!")
    print (s.get())

def updatecounter(n):
    n.set (n.get()+1)
    print (n.get())

#screen = tkinter.Tk()
screen = tk.Tk()
screen.title("Testing")
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
'''
# Team Selection
# v1 works
options_Teams = ["Red Sox","Yankees", "Blue Jays", "Rays", "Orioles", "Phillies"]
select_HomeTeam = tk.StringVar(screen)
select_VisitingTeam = tk.StringVar(screen)
visitingteamoptions = options_Teams
hometeamoptions = options_Teams
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


field_height = 600
field_width = 900
field = tk.Canvas(screen,height=field_height,width=field_width)
#field.grid(column=0,row=1,sticky=(W,E))
field.grid(column=0,row=1)

y = int(field_height/4)
x = int(field_width/4)
diamond = (2*x,y, 3*x,2*y, 2*x,3*y, x,2*y)
field.create_rectangle(0 , 0 , field_width, field_height, fill='blue')
field.create_polygon(diamond, fill='green')

'''
'''
message_frame = ttk.Frame(screen,width=(field_width/3)).grid(column=0,row=0)
s = StringVar()
s.set("String original")
message = ttk.Label(message_frame,textselectedHomeTeam=s).grid(column=0,row=0, sticky=E)
playButton = ttk.Butto_message_frame, text="Play", command=lambda: updatemessage(s)).grid(column=0,row=0,sticky=W)
'''
'''
counter_frame = tk.Frame(screen,width=300)
counter_frame.grid(column=0,row=0)
counter_frame.grid_columnconfigure(0,minsize=1200)
n = tk.IntVar()
n.set(1)
counting = tk.Label(counter_frame, textselectedHomeTeam=n, background="#ECECEC").grid(column=1,row=0)
countButton = tk.Button_ounter_frame, background="#ECECEC", text="Count", command=lambda: updatecounter(n)).grid(column=0,row=0)
'''
'''
test_frame = ttk.Frame(screen,width=(field_width/3)).grid(column=2,row=0,sticky=N)
style = ttk.Style()
L1 = ttk.Label(test_frame, text="Label Test")
L1.grid(column=0,row=0,sticky=W)
'''
screen.mainloop()