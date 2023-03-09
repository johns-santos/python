import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

## 1) Create a turtle that starts at the bottom of the screen 
player = Player()
car_manager = CarManager()

## 2) Listen for the "UP" keypress
screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_back, "Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    
    
    
    
