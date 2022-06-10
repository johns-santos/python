import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
user_choice = int(input('Select "0" for ROCK, "1" for PAPER, or "2" for SCISSORS\n'))
computer_choice = random.randint(0,2)

list = ["rock", "paper", "scissors"]
list2 = [rock, paper, scissors]

if(user_choice >= 3 or user_choice < 0):
    print("You selected an INVALID option")
else:
    print(f"\nYou selected: {list[user_choice]}")
    print(list2[user_choice])
    print(f"\nComputer selected: {list[computer_choice]}")
    print(list2[computer_choice])


if((user_choice == 0 and computer_choice == 2)
or (user_choice == 1 and computer_choice == 0)
or (user_choice == 2 and computer_choice == 1)
):
    print(f"\nYou Win, with {list[user_choice]}!!!!\n")

elif(user_choice == computer_choice):
    print("\nWe have a DRAW... :(\n")

elif((user_choice == 2 and computer_choice == 0)
or (user_choice == 0 and computer_choice == 1)
or (user_choice == 1 and computer_choice == 2)):
    print(f"\nComputer wins with {list[computer_choice]}. Try Again\n")
    