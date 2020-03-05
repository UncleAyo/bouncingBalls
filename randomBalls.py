from processing import *
from Screen import Screen
screen=Screen()
sizeX=1000
sizeY=800
count=0
def setup():
    size(sizeX,sizeY)
    fill(randint(0,255), randint(0,255),randint(0,255))
    
    
def draw():
   
    background(200)
    if mousePressed:
         
         screen.addBall()
    
    for i in screen.ball_list:
        
        i.display()
        
        i.update()
        i.isFallen()


run()