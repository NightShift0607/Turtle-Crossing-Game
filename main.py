from turtle import Screen
from time import sleep
from player import Player


# screen setup
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Cross The Turtle")
screen.tracer(0)


# player setup
player = Player()


# player movement
screen.listen()
screen.onkeypress(player.up, "Up")


# gameplay control
game_on = True
while game_on:
    screen.update()
    sleep(0.1)


# To make screen stay
screen.exitonclick()