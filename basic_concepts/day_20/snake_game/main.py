from snake import Snake
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Collide")
# Turn off tracer
screen.tracer(0)

snake = Snake()

# Make snake move - forward
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


####===== TASK LEFT TO-DO 
# Control snake across screen

# Create food & detect collision with food

# Create scoreboard

# Detect collision with wall - Game over

# Detect collision with tail - Game over



screen.exitonclick()