import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Staes Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()

# conver csv data to panda dataframe
data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    # Grab user guess and cover to TITLE case
    guess = answer_state.title()

    # Iterate Over data and find a match.
    if guess in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    

# Code to paste State name on map according to X,Y cordinates
def get_mouse_click_coor(x,y):
    print(x,y)
    
# Event listener waiting for click
turtle.onscreenclick(get_mouse_click_coor)

# Keep screen open after code executes
turtle.mainloop()