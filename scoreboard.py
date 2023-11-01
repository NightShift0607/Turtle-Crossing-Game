from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lev = 1
        self.level()
    
    
    def level(self):
        self.clear()
        self.goto(-280,260)
        self.write(f"Level: {self.lev}", align="left", font=("Courier", 20, "normal"))
    
    
    def update_level(self):
        self.lev += 1
        self.level()
    
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))