#import pygame
#pygame.init()

class Settings():
    def __init__(self):
        # Screen Settings
        self.size = 700, 500
        self.caption = "Tkinter Baseball"
        self.diamond_color = "#476042"
        #self.sb_of_font = tkFont.nametofont("TkDefaultFont")
        #sb_of_font.configure(size=48)
        
        #self.sb_of_font = pygame.font.SysFont('Calibri', 25, True, False )