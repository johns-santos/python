from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "black", "green", "blue", "purple"]
all_turtles = []

s = -90
for turtle_index in range(len(colors)):
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(colors[turtle_index])
    turtle_name.penup()
    turtle_name.goto(x=-240,y=int(s))
    all_turtles.append(turtle_name)
    s+=40
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win!!!!. The {winning_color} turtle is the winner")
            else:
                print(f"You Lose. The {winning_color} turtle is the winner")
        
        move_forward = random.randint(0, 10)
        turtle.forward(move_forward)
        
    
    

screen.exitonclick()