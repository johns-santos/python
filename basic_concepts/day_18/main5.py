
from turtle import Turtle, Screen
import random

s = Screen()
s.colormode(255)
t = Turtle()
t.pensize(2)
t.speed("fastest")

def main():
    gyro(7)

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def gyro(space_size):
  for _ in range(int(360 / space_size)):
      t.circle(100)
      t.setheading(t.heading() + space_size)
      t.pencolor(random_color())
   

if __name__ == '__main__':
    main()

s.exitonclick()
