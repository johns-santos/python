from turtle import Turtle, Screen


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.shapesize(5,5,12)
timmy.color("green")
timmy.forward(100)



john = Turtle()
print(john)
john.shape("turtle")
john.shapesize(5,5,12) 
john.color("red")
john.backward(150)



my_screen = Screen()
my_screen.canvheight = 500
# Prints screen hieght attribute
print(my_screen.canvheight)
# Method that allows code to run until clicked.
my_screen.exitonclick()


num = "5"
num = int(num)
