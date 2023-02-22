from turtle import Turtle,Screen
import random

s = Screen()
s.colormode(255)
s.bgcolor("black")

t = Turtle()
t.hideturtle()
t.shape("arrow")
t.speed("fastest")

for i in range(300):
   
    # t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    # t.circle(i)
    
    # t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    # t.circle(i*0.8)
    # t.right(3)
    # t.forward(3)
    
    # t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    t.color("red")
    t.circle(i*0.8)
    t.right(3)
    t.forward(3)


s.exitonclick()