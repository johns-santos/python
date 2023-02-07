
from turtle import Turtle, Screen

from turtle import Turtle
from turtle import Screen

# Required in order to open window
screen = Screen()
screen.colormode(255)


tim = Turtle()
tim.shape("turtle")
tim.color(139, 0, 139)

for _ in range(0,4):
    tim.left(90)
    tim.forward(100)



screen.exitonclick()