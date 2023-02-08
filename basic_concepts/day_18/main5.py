
from turtle import Turtle, Screen
import random

s = Screen()
s.colormode(255)
t = Turtle()
t.pensize(2)
t.speed("fastest")

def main():
    gyro()

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def gyro():
    for i in range(0,360):
        t.circle(60)
        t.left(20)
        t.forward(1)
        t.pencolor(random_color())
       

if __name__ == '__main__':
    main()

s.exitonclick()
