############### Blackjack Project #####################
import random
from replit import clear
from art import logo

# Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Create a function called calculate_score() that takes a List of cards as input and returns the score. sum() 
#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in card_list and sum(card_list) > 2:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list) 

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "\nDraw   :\ \n"
    elif computer_score == 0:
        return "\n🥲 Lose, opponent has Blackjack 🥲\n"
    elif user_score == 0:
        return "\n😎 Win with a Blackjack!!!! 😎\n"
    elif user_score > 21:
        return "\n🥲 You went over. You lose 🥲\n"
    elif computer_score > 21:
        return f"\nOpponent went over. You win!! 😁\n Opponent score {computer_score}\n"
    elif user_score > computer_score:
        return "\n😁 You win 😁\n"
    else:
        return "\n🥲 You Lose  🥲\n"

def play_game():
    print(logo)
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.#
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print (f"Your Hand: {user_cards}  Your Score: {user_score}")
        print (f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        #Step 10: If the game has not ended, ask the user if they want to draw  another card. If yes, then use the deal_card() function to add another   card to the user_cards List. If no, then the game has ended.
        else:
            user_should_deal = input ("\nType 'y' to draw another card, type 'n'  to pass: \n")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Step 12: COMPUTER SCORE - Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()