# Classes (screen, paddle, ball, scoreboard)
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle((478, 0))
l_paddle = Paddle((-480, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()
    ball.move()
    
    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        print(ball.speed())
        ball.bounce_y()
        
    # Detect collision with paddle  
    if ball.distance(r_paddle) < 40 and ball.xcor() > 460 or ball.distance(l_paddle) < 40 and ball.xcor() < -460:
        ball.bounce_x()
    
    # Detect R paddle misses 
    if ball.xcor() > 490:
        ball.reset_position()
        screen.bgcolor("red")
        time.sleep(1) 
        scoreboard.l_point()
        screen.bgcolor("black")
        
          
    # Detect L paddle misses    
    if ball.xcor() < -490:
        ball.reset_position()
        screen.bgcolor("red")
        time.sleep(1) 
        scoreboard.r_point()
        screen.bgcolor("black")
        
 

screen.exitonclick()