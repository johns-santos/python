from dis import dis
from email import contentmanager
from lib2to3.pytree import LeafPattern
from operator import contains
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




end_of_game = False
# Generate a random word
hint = ["What can’t talk but will reply when spoken to?",
"The more of this there is, the less you see. What is it?",
"I have branches, but no fruit, trunk or leaves. What am I?",
"Poor people have it. Rich people need it. If you eat it you die. What is it?",
"Spelled forwards I’m what you do every day, spelled backward I’m something you hate. What am I?"]
word_list = ["echo", "darkness", "bank","nothing","live"]
# Generate blanks required for each letter in word
chosen_word = random.choice(word_list).lower()
lives = 6

hint_index = word_list.index(chosen_word)

print("\n===========================================")
print(f"HINT: {hint[hint_index]}")
print("===========================================\n")


display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)


# Allow user to guess until blanks are eliminated
while not end_of_game:
    user_guess = input("\nGuess a letter: \n ").lower()
        
    #CHECK GUESS - if CORRECT replace blank with letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
            
    print(display)


# If "_" have been eliminated end game
    if "_" not in display:
        end_of_game = True
        print("\n===========================================")
        print("You WIN!!!!")
        print("===========================================\n")

    if user_guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print(stages[lives])
                print("\n===========================================")
                print(f"{lives} lives remaing")
                print("You LOSE!!!!")
                print("===========================================\n")
                break

    if lives > 0:
      print(f"\nHINT: {hint[hint_index]}\n")
      print("\n===========================================")
      print(f"{lives} lives remaing")
      print("===========================================\n")
    else:
      break

   
            



