
# Get degree by (360 / num_of_sides)
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("arrow")
tim.pensize(3)
tim.pencolor("")


def main():
    shape(3,40,120,"blue")
    shape(4,40,90,"black")
    shape(5,40,72,"red")
    shape(6,40,60,"cyan")
    shape(7,40,51.42,"magenta")
    shape(8,40,45,"purple")
    shape(9,40,40,"pink")
    shape(10,40,36,"green")
    
def shape(side, steps, degree, color):
    for _ in range(side):
        tim.pencolor(color)
        tim.forward(steps)
        tim.right(degree)
        tim.forward(steps)

if __name__ == "__main__":
    main()
    
screen.exitonclick()