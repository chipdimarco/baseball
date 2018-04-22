# Settings

class Settings():
    def __init__(self):
        # Screen Settings
        self.width = 900
        self.height = 600
        self.size = (f'{self.width}x{self.height}')
        self.caption = "Tkinter Baseball"
        self.diamond_color = "#4DBD33"  #4A777A
        self.inning = 1
        self.half_inning = "Top"
        self.visitor_leads_off_inning = 0
        self.home_leads_off_inning = 0
        # If console_mode is True, the Tkinter interface is skipped
        self.console_mode = False
        # If stored_rosters is True, access data locally, not on line
        self.stored_rosters = True
        self.done = False
        self.screen_background = "#ECECEC"
        self.team_codes = {
            'Red Sox':'bos',
            'Yankees':'nyy',
            'Cubs':'chc',
            'Rays':'tb',
            'Astros':'hou',
            'Phillies':'phi'
        }
        self.use_dh = True


