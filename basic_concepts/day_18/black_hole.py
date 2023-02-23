from turtle import Turtle, Screen
import random


s = Screen()
s.bgcolor('black')
s.colormode(255)

t = Turtle()
t.shape("circle")

for _ in range(120):
    t.speed("fastest")
    t.forward(180)
    t.left(70)
    t.forward(100)
    t.right(60)
    t.penup
    t.setposition(0,0)
    t.pendown
    t.right(5)
    t.pencolor(random.randint(0,255), random.randint(0,255),random.randint(0,255))
    
    
s.exitonclick()