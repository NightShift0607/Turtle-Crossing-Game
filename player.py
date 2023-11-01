from turtle import Turtle
XCOR = 0
YCOR = -280
DIST = 20


class Player:
    def __init__(self):
        self.player = Turtle("turtle")
        self.create_player()
    
    
    def create_player(self):
        self.player.setheading(90)
        self.player.penup()
        self.player.goto(XCOR,YCOR)
    
    
    def up(self):
        self.player.forward(DIST)