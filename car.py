from turtle import *
from random import randint
XCOR = 310
DIST = 20


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.random_color()
        self.setheading(180)
        self.random_location()
    
    
    def random_color(self):
        colormode(255)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        col =  (r, g, b)
        self.color(col)
    
    
    def random_location(self):
        ycor = randint(-250,280)
        self.goto(XCOR,ycor)
    
    
    def move_car(self):
        self.forward(DIST)