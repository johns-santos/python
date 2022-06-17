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
word_list = ["Sunray", "vacation", "Christmas", "Marine", "apple", "rocky"]
# Generate blanks required for each letter in word
chosen_word = random.choice(word_list).lower()
lives = 6



print(f"Solution: {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)


# Allow user to guess until blanks are eliminated
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()
        
    #CHECK GUESS - if CORRECT replace blank with letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
            
    print(display)


# If "_" have been eliminated end game
    if "_" not in display:
        end_of_game = True
        print("You Win!!!!")

    if user_guess not in chosen_word:
            lives = lives - 1
            print(stages[lives+1])

    if lives == 0:
        print(stages[lives])
        print("You Lose!")
        break


    
    print(lives)

   
            



