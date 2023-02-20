from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


# Create listener
screen.listen()
# Bind keystroke to listener
screen.onkey(key="space", fun=move_forwards)




screen.exitonclick()