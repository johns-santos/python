import random

# Generate a {random} number between 1 and 10
num = random.randint(1, 10)
print(num)
# Ask user {name}
name = input("What is your name? ").title()
print(name)
# Then ask {name} to guess {number} between 1 and 10.
user_guess = int(input(f"Well, {name}, I am thinking of a number between 1 and 10. \nWhat number am I thinking of? "))

correct_guess = False
guess_count = 0

while correct_guess == False:

    # If {number} is greater than {random} print: "You're guess is too high."
    if user_guess > num:
        print(f"Your guess is too high.")
        guess_count += 1
        user_guess = int(input("Take another guess: "))
        # Else if {number} is less than {random}, print: "You're guess is too low."
    elif user_guess < num:
        print(f"Your guess is too lower.")
        guess_count += 1
        user_guess = int(input("Take another guess: "))
# Else print, "Good job, {name}! You're guessed the my number in {x} guess!"
    else: 
        guess_count += 1
        print(f"Good job, {name}. You guessed {num} in {guess_count} guesses!")
        correct_guess = True
