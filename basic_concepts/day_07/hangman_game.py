from replit import clear
import random
import hangman_asciiart
import hangman_words

end_of_game = False
# Generate a random word
chosen_word = random.choice(hangman_words.word_list).lower()
lives = 6
hint_index = hangman_words.word_list.index(chosen_word)
print(f"{hangman_asciiart.logo}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"


# Allow user to guess until blanks are eliminated
while not end_of_game:
    print("\n===============: HINT :====================")
    print(f"Clue: {hangman_words.word_hint[hint_index]}")
    print(f"{word_length} - Letter word : {' '.join(display)}")
    print("===========================================")
    print(f"{hangman_asciiart.stages[lives]}\n{lives} - attempt(s) remaining")

    user_guess = input("\nGuess a letter: \n ").lower()
    clear()

    if user_guess in display:
      print(f"'Letter has already been selected.")
         
    #CHECK GUESS - if CORRECT replace blank with letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
            
    if user_guess not in chosen_word:
            lives -= 1
            # if lives != 0:
            #   print(f"\nHINT: {hangman_words.word_hint[hint_index]}\n")
            if lives == 0:
                print(hangman_asciiart.stages[lives])
                print("\n===========================================")
                print(f"{lives} attempt(s) remaining")
                print("You LOSE!!!! - GAME OVER")
                print("=========================================")
                break

    # If "_" have been eliminated end game
    if "_" not in display:
        end_of_game = True
        print("\n=============================================")
        print("You WIN!!!!")
        print("=============================================\n")