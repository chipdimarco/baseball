#import pygame
#pygame.init()

class Settings():
    def __init__(self):
        # Screen Settings
        self.width = 900
        self.height = 600
        self.size = (f'{self.width}x{self.height}')
        self.caption = "Tkinter Baseball"
        self.diamond_color = "#476042"
        self.inning = 1
        self.half_inning = "Top"
        self.visitor_leads_off_inning = 0
        self.home_leads_off_inning = 0
        # If console_mode is True, the Tkinter interface is skipped
        self.console_mode = True

        #self.done = False
        #self.sb_of_font = tkFont.nametofont("TkDefaultFont")
        #sb_of_font.configure(size=48)
        
        #self.sb_of_font = pygame.font.SysFont('Calibri', 25, True, False )