
# Get degree by (360 / num_of_sides)
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("arrow")
tim.pensize(3)
tim.pencolor("")


def main():
    shape(3,50,120,"blue")
    shape(4,50,90,"black")
    shape(5,50,72,"red")
    shape(6,50,60,"cyan")
    shape(7,50,51.42,"magenta")
    shape(8,50,45,"purple")
    shape(9,50,40,"pink")
    
def shape(side, steps, degree, color):
    for _ in range(side):
        tim.pencolor(color)
        tim.forward(steps)
        tim.right(degree)
        tim.forward(steps)

if __name__ == "__main__":
    main()
    
screen.exitonclick()