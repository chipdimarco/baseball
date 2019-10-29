import sys
#import pygame
#import tkinter
from game_settings import Settings

settings = Settings()

def doSomething():
    print ("Do Something")
    return("Did Something")

def done(done):
    return (not done)

def print_lineup_box (lineup_box):
    for inning in lineup_box:
        for x in inning:
            print (x)


# PYGAME FUNCTIONS BELOW
# INACTIVE
'''
# Respond to KEYDOWN
def check_keydown_events(event, settings, screen):
    if event.key == pygame.K_RIGHT:
        #something.moving_right = True
        return("right")
    elif event.key == pygame.K_LEFT:
        #something.moving_left = True
        return("left")
    elif event.key == pygame.K_SPACE:
        return("pitch")
    elif event.key == pygame.K_q:
        #sys.exit()
        pygame.quit()
        
def check_events(settings, screen):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            sys.exit()
        # KEYDOWN
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen)
        # KEYUP
        elif event.type == pygame.KEYUP:
            # check_keyup_events(event, ship)
            return ("keyup")
'''
    
'''    
def draw_field(screen, color):
    # Foul Lines
    pygame.draw.aaline(screen, color, [0,100], [350,450] ) 
    pygame.draw.aaline(screen, color, [350,450], [700,100] ) 
    #pygame.draw.aaline(screen, WHITE, [0,100], [350,450] ) 
    #pygame.draw.aaline(screen, WHITE, [350,450], [700,100] ) 
        
    # Bases 2nd/1st/H/3rd
    pygame.draw.rect(screen, color, [340,260,20,20],0)
    pygame.draw.rect(screen, color, [420,340,20,20],0)
    pygame.draw.rect(screen, color, [340,440,20,20],0)
    pygame.draw.rect(screen, color, [260,340,20,20],0)
        
    # Pitchers mound
    pygame.draw.circle(screen, color, (350, 350), 30 , 3)
        
    # Infield arc
    pygame.draw.arc(screen, color, [215,200,260,225], 0, 3.14, 2)
'''
        
        
'''    
def draw_scoreboards(screen, color, color_center,v_score,h_score):
        
    # Scoreboard in outfield
    pygame.draw.rect(screen, color, [50,5,150,50] )
    pygame.draw.rect(screen, color_center, [250,5,200,50])
    pygame.draw.rect(screen, color, [500,5,150,50])
        
    # Outfield Scoreboards
    v_sb_score = settings.sb_of_font.render("Visitor " + str(v_score), True, color_center)
    h_sb_score = settings.sb_of_font.render("Home " + str(h_score), True, color_center)
    screen.blit(v_sb_score, [55,20])
    screen.blit(h_sb_score, [505,20])
'''

"""
# REVISE THIS TO USE THE Lineup() class
def set_v_lineup():
    v_lineup = ['BOSTON','Pedroia','Benintendi','Betts','Ramirez','Bogaerts',
                    'Moreland','Sandoval','Bradley','Vazquez']
    return v_lineup

# REVISE THIS TO USE THE Lineup() class
def set_h_lineup():
    h_lineup = ['NEW YORK', 'Garner','Sanchez','Bird','Holliday','Ellsbury',
                    'Castro', 'Headley','Judge','Torreyes']
    return h_lineup
"""