import colorama
from art import logo, vs
from random import randint
from game_data import data

def main():
    turn()
    
def randomChoice():
    randChoice = randint(0, (len(data) - 1))
    return randChoice
   

def turn():
    wrong = 3
    point = 0 
    
    # Repeat game until user has three wrond guesses. 
    while wrong != 0:
        choice_01 = randomChoice()
        choice_02 = randomChoice()
        # Generate a new value for "CHOICE_02" if it is that same as "CHOICE_01"
        while choice_01 == choice_02:
            choice_02 = randomChoice()
        
        # Display art and compare statements 
        print(f"{logo} \nCompare A: {data[choice_01]['name']}, a {data[choice_01]['description']}, from {data[choice_01]['country']}.")
        print(f"{vs} \nAgainst B: {data[choice_02]['name']}, a {data[choice_02]['description']}, from {data[choice_02]['country']}.")
        
        # Ask user for guess input
        choice = (input("\nWho has more followers? Type 'A' or 'B': ")).lower()
        A = data[choice_01]["follower_count"]
        B = data[choice_02]["follower_count"]
        
        # Check if user guess it correct.    
        if choice == "a" and A > B:
            point += 1
            # Print SCORE and REMAINING ATTEMPTS
            print(colorama.Fore.GREEN + f"You're Right. Score: {point}. Chances Remaining: {wrong}." + colorama.Fore.RESET)           
        elif choice != "a" and B > A:
            point += 1
            print(colorama.Fore.GREEN +f"\nYou're right. Score: {point}. Chances Remaining: {wrong}.\n"+ colorama.Fore.RESET)
        else:
            wrong -= 1
            print(colorama.Fore.RED +f"\nWrong! Score: {point}. Chances Remaining: {wrong}.\n"+ colorama.Fore.RESET)
    
    # Provide user with end SCORE.        
    print(colorama.Fore.BLUE + f"\nTotal Points: {point}\n"+ colorama.Fore.RESET)
        
main()
