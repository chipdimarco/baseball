from tkinter import *
from tkinter import ttk

# function that takes the value and updates it with set
def updatemessage(s):
    s.set ("Update!")
    print (s.get())

def updatecounter(n):
    n.set (n.get()+1)
    print (n.get())

screen = Tk()
screen.title("Testing")

field_height = 600
field_width = 900
field = Canvas(screen,height=field_height,width=field_width)
field.grid(column=0,row=1,sticky=(W,E))

y = int(field_height/4)
x = int(field_width/4)
diamond = (2*x,y, 3*x,2*y, 2*x,3*y, x,2*y)
field.create_rectangle(0 , 0 , field_width, field_height, fill='blue')
field.create_polygon(diamond, fill='green')

s = StringVar()
s.set("String original")

message = ttk.Label(screen,textvariable=s).grid(column=0,row=2)
playButton = ttk.Button(screen, text="Play", command=lambda: updatemessage(s)).grid(column=0,row=0)

n = IntVar()
n.set(1)
counting = ttk.Label(screen, textvariable=n).grid(column=1,row=2)
countButtong = ttk.Button(screen, text="Count", command=lambda: updatecounter(n)).grid(column=1,row=0)


screen.mainloop()