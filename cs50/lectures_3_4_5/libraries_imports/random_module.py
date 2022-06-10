# Import function from module 
import random 
import statistics

print("\n==== RANDOM ======")
# Use 'choice' function from 'random' module
coin = random.choice(["heads", "tails"])
print(coin)

print("\n===============")
# Randint function of random
num = random.randint(1, 2)
print(num)

print("\n===============")
# Shuffle function of random - shuffles in place - mutates list
cards = ['jack', 'queen', 'king']
shuffled_deck = random.shuffle(cards)

#FOR loop to return one at a time in shuffled order
for card in cards:
    print(card)


print("\n===============")
print(cards)



print("\n====statistics=======")

avg = statistics.mean([98, 86, 88, 92, 76, 68])
print(avg)

