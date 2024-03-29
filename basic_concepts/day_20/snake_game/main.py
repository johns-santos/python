from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Collide")

# Turn off tracer
screen.tracer(0)

snake = Snake()
# 3) Create food
food = Food()
# 5) Create scoreboard
scoreboard = ScoreBoard()
   
#2) Control snake across screen  
screen.listen() 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down") 
screen.onkey(snake.left, "Left") 
screen.onkey(snake.right, "Right") 

#1) Make snake move - forward
game_on = True
while game_on:
    # Refresh
    screen.update()
    # Refresh control rate
    time.sleep(0.1)
    snake.move()
    
    # 4) detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        # 5) Refresh scoreboard
        scoreboard.increase_score()
        
    #6) Detect collision with wall - Game over
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 295 or snake.head.ycor() < -299:
        scoreboard.reset()
        snake.snake_reset()
        
    # Detect collision with tail - Use slicing to start loop from second segment
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.snake_reset()
               
screen.exitonclick()