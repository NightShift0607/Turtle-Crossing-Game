from turtle import Screen
from time import sleep
from random import randint
from player import Player
from car import Car
from scoreboard import Scoreboard
cars = []

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


# Cars setup
def setup_cars():
    car = Car()
    cars.append(car)


# Scoreboard setup
score = Scoreboard()


# gameplay control
game_on = True
i = 1
while game_on:
    screen.update()
    sleep(player.car_speed)
    if i%3 == 0:
        setup_cars()
    
    for car in cars:
        car.move_car()
        if player.player.distance(car) <= 20:
            game_on = False
            score.game_over()
    
    if player.player.ycor() > 290:
        player.next_level()
        score.update_level()
    i +=1


# To make screen stay
screen.exitonclick()