# 3/17/2018
# help from pythonprogramming.net
import tkinter as tk
LARGE_FONT = ("verdana",14)

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
        label = tk.Label(self,text="Splash Page",font=LARGE_FONT)
        label.pack()
        
        button_setup = tk.Button(self, text="Go to Setup",
            command = lambda: controller.show_frame(Setup))
        button_setup.pack()

        button_play = tk.Button(self, text="Go to Play",
            command = lambda: controller.show_frame(Play))
        button_play.pack()


class Setup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Setup", font=LARGE_FONT)
        label.pack()
        button_splash = tk.Button(self, text="Go to Splash",
            command = lambda: controller.show_frame(Splash))
        button_splash.pack()
        
        button_play = tk.Button(self, text="Go to Play",
            command = lambda: controller.show_frame(Play))
        button_play.pack()

class Play(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Play", font=LARGE_FONT)
        label.pack()
        button_splash = tk.Button(self, text="Go to Splash",
            command = lambda: controller.show_frame(Splash))
        button_splash.pack()

        button_setup = tk.Button(self, text="Go to Setup",
            command = lambda: controller.show_frame(Setup))
        button_setup.pack()




'''
# call this from baseball.py
app = GameScreen()
app.mainloop()
'''