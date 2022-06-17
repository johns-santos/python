#===============================================================
# ================ EXERCISE 1 - HURDLE 1 & 2
#===============================================================
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for x in range(1,6):
while at_goal() != True:
    jump()


#===============================================================
# ================ EXERCISE 2 - HURDLE 3 - RANDOM HURDLES......
#===============================================================
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
   
    
#for x in range(1,6):
while at_goal() != True:  
    if front_is_clear() != True:
        jump()
    else:
        move()


#===============================================================
# ================ EXERCISE 2 - HURDLE 4 - RANDOM HURDLES......
#===============================================================

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
   
    
#for x in range(1,6):
while at_goal() != True:  
    if front_is_clear() != True:
        jump()
    else:
        move()