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
#screen.configure(background="#e8e8e8")
screen.configure(background="#ECECEC")

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
message_frame = ttk.Frame(screen,width=(field_width/3)).grid(column=0,row=0)
s = StringVar()
s.set("String original")
message = ttk.Label(message_frame,textvariable=s).grid(column=0,row=0, sticky=E)
playButton = ttk.Button(message_frame, text="Play", command=lambda: updatemessage(s)).grid(column=0,row=0,sticky=W)
'''

counter_frame = tk.Frame(screen,width=300).grid(column=0,row=0)
n = tk.IntVar()
n.set(1)
counting = tk.Label(counter_frame, textvariable=n, background="#ECECEC").grid(column=1,row=0)
countButton = tk.Button(counter_frame, background="#ECECEC", text="Count", command=lambda: updatecounter(n)).grid(column=0,row=0)
'''
test_frame = ttk.Frame(screen,width=(field_width/3)).grid(column=2,row=0,sticky=N)
style = ttk.Style()
L1 = ttk.Label(test_frame, text="Label Test")
L1.grid(column=0,row=0,sticky=W)
'''
screen.mainloop()