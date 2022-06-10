
print('''
     ______  ____     ___   ____  _____ __ __  ____     ___      ____  _____ _       ____  ____   ___   
|      T|    \   /  _] /    T/ ___/|  T  T|    \   /  _]    l    j/ ___/| T     /    T|    \ |   \  
|      ||  D  ) /  [_ Y  o  (   \_ |  |  ||  D  ) /  [_      |  T(   \_ | |    Y  o  ||  _  Y|    \ 
l_j  l_j|    / Y    _]|     |\__  T|  |  ||    / Y    _]     |  | \__  T| l___ |     ||  |  ||  D  Y
  |  |  |    \ |   [_ |  _  |/  \ ||  :  ||    \ |   [_      |  | /  \ ||     T|  _  ||  |  ||     |
  |  |  |  .  Y|     T|  |  |\    |l     ||  .  Y|     T     j  l \    ||     ||  |  ||  |  ||     |
  l__j  l__j\_jl_____jl__j__j \___j \__,_jl__j\_jl_____j    |____j \___jl_____jl__j__jl__j__jl_____j''')

print("\nWelcome to Treasure Island. Your mission is to find the treausre.\n")

chest = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''


win = "\nYou found the treasure! You win!!!!!\n\n"
lose = "Game Over"
step_01 = str(input('\nAfter leaving home and reaching the forrest, you come to a crossroads. \nWhich way do you want to go?\n\n Enter "LEFT" or "RIGHT"\n\n').lower())

if(step_01 == "left"):
    step_02 = str(input('\nAfter walking several miles you reach a flooded stream. \nDo you want to swim or wait for a boat?\n\n "Enter SWIM" or "WAIT" \n\n').lower())
    if(step_02 == "wait"):
        step_03 = str(input('\nSuccessfully across the river. You see a castle on a hill. \nWhen you reach the castle you see three doors and a sign. \nThe doors are painted three different colors and the sign reads, \n"Choose carefully!!!"\n\n Enter "RED", "BLUE", or "YELLOW" \n\n').lower())
        if(step_03 == "red"):
            print(f"\nOh no!!! You've been burned by fire. {lose}")
        elif(step_03 != "yellow"):
            print(f"\nOh no!!! You've been eaten by beast! {lose}")
        else: 
            print(f"{win}\n {chest}")
    else:
        print(f"\nOh no!!! You've been attacked by trout! {lose}")
else:
    print(f"\nOh no!!! You have fallen into a hole! {lose}")
