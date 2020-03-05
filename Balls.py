from random import randint
from processing import *
class Ball:
    
    def __init__(self):
        self.xpos=mouseX
        self.ypos=mouseY
        self.vel= 0
        #gravities=[0.1,0.2,0.3]
        self.gravity =0.1 #gravities[randint(0,len(gravities)-1)]
        self.rad= randint(10,200)
        self.colour=color(randint(0,255), randint(0,255),randint(0,255))
        
    def update(self):
        self.ypos+=self.vel
        self.vel+=self.gravity
    def display(self):
        fill(self.colour)
        ellipse(self.xpos, self.ypos, self.rad,self.rad)
    def isFallen(self):
        
        if self.ypos > sizeY-(self.rad/2):
            self.vel*=-0.55
            self.ypos=sizeY - (self.rad/2)
    
        
            
    
    def run(self):
        Ball().display()
        


    
        


    