
# First attempt
def prime_checker(number):
    i = 0
    count = 0
    prime = False   
    while i <= number:
        i = i + 1
        if number % i == 0 and number > 0 and number != 1:
            count = 1 + count
            print(f"{i} *** divides evenly into {number} ***")
            if count <= 2:
                prime = True
            else:
                prime = False
    if prime == True:
        print(f"{number} is a PRIME number")
    else:
        print(f"{number} is NOT a PRIME number")


# Shorter however does not check negNums, zero, or one.
def prime_checker_01(number):
    is_prime = True
    # Check all numbers between 2 and the specified number but not including the number.
    for i in range(2, number):
        if number % i == 0:
            print(f"{i} divides evenly into {number}")
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

#Write your code above this line 👆
#Do NOT change any of the code below👇
n = int(input("Check this number: "))

print("\n --- First attempt ---")
prime_checker(number=n)

print("\n --- Second attempt ---")
prime_checker_01(number=n)



