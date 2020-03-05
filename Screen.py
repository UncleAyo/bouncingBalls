from Balls import Ball
class Screen:

    def __init__(self):
        self.ball_list=[]
        
    def addBall(self):
    
        self.ball_list.append(Ball())
        
            #if i.ypos+((i.rad)/2) == sizeY:
                #i.isFallen()