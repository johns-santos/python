import random

print("Hello. What is your name? ")
name = input().title()

print("Guess a number between 1 and 20. You have 6 guess. ")

secret_num = random.randint(1, 20)
print(secret_num)

for guessesTaken in range(1,7):
    print("Take a guess: ")
    user_guess = int(input())

    if user_guess < secret_num:
        print('Your guess is too low.\n')
    elif user_guess > secret_num:
        print('Your guess is too high.\n')
    else:
        break 


if user_guess == secret_num:
    print(f'\nGood job {name}. You took {guessesTaken} guesses!!!\n')
else:
    print(f"\nSorry, {name}, I was thinking of the number {secret_num}.\n")

