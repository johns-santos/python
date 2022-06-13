import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_list = []
random_letters = random.choices(letters, k=nr_letters)
for l in random_letters:
    random_list.append(l)

random_symbols = random.choices(symbols, k=nr_symbols)
for s in random_symbols:
    random_list.append(s)

random_numbers = random.choices(numbers, k=nr_numbers)
for n in random_numbers:
    random_list.append(n)


# first attempt
random.shuffle(random_list)
password = ''.join(random_list)
print(password)


# second attemp
new_list = random_letters + random_symbols + random_numbers
print(new_list)
random.shuffle(new_list)
password1 = ''.join(new_list)
print(password1)








