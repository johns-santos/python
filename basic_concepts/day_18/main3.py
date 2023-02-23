from turtle import Turtle,Screen
import  random

screen = Screen()
screen.colormode(255)
tim = Turtle()
colors = ['red', 'pink', 'black', 'blue', 'magenta', 'cyan','purple','orange', 'green']

def main():
    num_of_shapes()
  
def get_shape(side):
    angle = 360 / side
<<<<<<< HEAD
    for _ in range(side):
        tim.pencolor(random.choice(colors))
=======
    tim.pencolor(random.choice(colors))
    for _ in range(side):
>>>>>>> Master (#7)
        tim.forward(50)
        tim.right(angle)
         
def num_of_shapes():
    for _ in range(3,11):
        get_shape(_)
       
if __name__ == "__main__":
    main()
    
screen.exitonclick()