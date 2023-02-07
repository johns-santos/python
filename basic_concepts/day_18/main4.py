from turtle import Turtle, Screen
import random

screen = Screen()

t = Turtle()
t.pensize(10)

colors = ['red', 'pink', 'black', 'blue', 'magenta', 'cyan','purple','orange', 'green']
direction = [0, 90, 180, 270]


def random_walk(num):
    for i in range(1, num):
        t.color(random.choice(colors))
        t.forward(25)
        t.setheading(random.choice(direction))
        # t.speed(i++1)
        
random_walk(250)

screen.exitonclick()



