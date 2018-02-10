#import pygame
#pygame.init()

class Score():
    def __init__(self):
        self.inning = 1
        self.half = "top"
        self.v_score = 0
        self.h_score = 0
