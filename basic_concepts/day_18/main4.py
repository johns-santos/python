from turtle import Turtle, Screen
import random

screen = Screen()
# Color mode allows RGB range between 0 and 255.
screen.colormode(255)

t = Turtle()
t.pensize(10)
direction = [0,90,180, 270]
# colors = ['red', 'pink', 'black', 'blue', 'magenta', 'cyan','purple','orange', 'green']

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    

def random_walk(num):
    for i in range(1, num):
        # t.color(random.choice(colors))
        t.pencolor(random_color())
        t.forward(15)
        t.setheading(random.choice(direction))
        t.speed(i++1)
        
random_walk(500)

screen.exitonclick()



