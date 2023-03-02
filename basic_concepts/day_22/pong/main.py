# Classes (screen, paddle, ball, scoreboard)
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = 0
l_score = 0

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect with right paddle  
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()
    
    # Detect missed ball and game over
    if ball.xcor() > 390:
        ball.reset_position()
        
    if ball.xcor() < -390:
        ball.reset_position()
 
 # LEFT TO DO
 #8) Create scoreboard
# Keep score
# Count roundsw
# end game & Declare winner   

screen.exitonclick()