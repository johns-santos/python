from turtle import Turtle,  Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(5)
    
def move_backwards():
    tim.backward(5)
    
def move_left():
    tim.left(90)
    
def move_right():
    tim.right(90)

def clockwise():
    for x in range(180):
        tim.speed(x)
        tim.forward(1)
        tim.right(1)
        x+=1

def counter_clockwise():
    for x in range(180):
        tim.speed(x)
        tim.backward(1)
        tim.left(1)
        x+=2
        
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="f", fun=move_forwards)
screen.onkey(key="b", fun=move_backwards)
screen.onkey(key="C", fun=counter_clockwise)
screen.onkey(key="c", fun=clockwise)
screen.onkey(key="l", fun=move_left)
screen.onkey(key="r", fun=move_right)
screen.onkey(key="a", fun=clear_screen)

screen.exitonclick()