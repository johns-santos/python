import random
from asciArt import art
from colorama import Fore, Back, Style

# Game ASCI LOGO and random number generation
print(f"\n{art}\n")
print("Welcome to the number Guessing Game!")
number = random.randint(0, 50)
    
# Game function
def guessing_game():
    print("I am thinking of a number between 1 and 100.")
    guess = 0
    # Set difficulty level - I.E., Number of user guesses.
    diffculty = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
    if diffculty == "easy":
        guess_count = 10
        print(f"You have 10 guesses.")
    else:
        guess_count = 5
        print(f"You have 5 guesses.")
        # WHILE LOOP - while total guess is less than guess_count set by difficulty.
    while guess != guess_count:
        remaining_guesses = guess_count - guess
        
        try:
            user_guess = int(input("Pleaes guess a number: "))
            if user_guess < number:
                print(f"Your guess is to low. Take another guess. You have {remaining_guesses -1} guesses left.")
                guess += 1
            if user_guess > number:
                print(f"Your guess is to high. Take another guess. You have {remaining_guesses -1} guesses left.")
                guess += 1
            if user_guess == number:
                print(Fore.GREEN + f"\n Good GUESS!!! You guessed {number}.\n" + Style.RESET_ALL)
                break
            if guess_count == guess:
                print(f"\nYou have exceeded your guess limit.\n")
        except TypeError:
            print(Fore.RED + f"  *** ENTRY NOT VALID. Please enter a number between 1 and 100. " + Style.RESET_ALL)           
        except ValueError:
            print(Fore.RED + f"  *** ENTRY NOT VALID. Please enter a number between 1 and 100. " + Style.RESET_ALL)
           
        
        
guessing_game()
