# Settings
# 10-20-2019: Comment out Tkinter settings

class Settings():
    def __init__(self):
        # Screen Settings
        # self.name = "settings object"
        self.inning = 1
        self.half_inning = "Top"
        self.visitor_leads_off_inning = 0
        self.home_leads_off_inning = 0
        # If console_mode is True, the Tkinter interface is skipped
        self.console_mode = True
        self.PLAY_BY_PLAY = False
        self.verbose_mode = False
        # If stored_rosters is True, access data locally, not on line
        self.stored_rosters = True
        self.done = False
        self.use_dh = True


