############### Blackjack Project #####################
# REMAINING STEPS
#Step 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Step 11: The score will need to be rechecked with every new card drawn and the checks in Step 9 need to be repeated until the game ends.

#Step 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Step 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Step 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random

# Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#Create a function called calculate_score() that takes a List of cards as input and returns the score. sum() 
def calculate_score(card_list):
    return sum(card_list)
#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in card_list and sum(card_list) > 2:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list) 

# Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.#
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print (f"Your Hand: {user_cards}  Your Score: {user_score}")
print (f"Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True




