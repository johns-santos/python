# Classes (screen, paddle, ball, scoreboard)
from turtle import Turtle,Screen,hideturtle,showturtle
from paddle import Paddle
import time

#1)  Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


  
#2) Create paddle class
# Create contorl for user paddle
#3) Create automated paddle
#4) Create ball
# Make ball move around screen

#5) Detect collision with wall and bounce

#6) Detect collision with paddle and bounce

#7) Detect when paddle misses ball


#8) Create scoreboard
# Keep score
# Count rounds
# end game & Declare winner

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # Refresh
    # time.sleep(0.1)
    # Refresh control rate
    screen.update()

screen.exitonclick()