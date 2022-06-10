import random

randInt = random.randint(0, 1)
coin = ['heads', 'tails']
question = input('Please enter: "Heads" or "Tails"\n').lower()


if(question == coin[randInt]):
  print(f"You WIN! : \n You choose: {question} - Computer choose: {coin[randInt]}")
else:
  print(f"YOU LOOSE!!!!!!!! BOOO!!!\n  You choose: {question} - Computer choose: {coin[randInt]}")