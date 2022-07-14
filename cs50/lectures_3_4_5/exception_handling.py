# Handle exceptions with a TRY/EXCEPT block

# While an "exception" is TRUE loop
while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        print('"X" is not an integer')
    # Break out of loop if "exception is FALSE"
    else:
        break

print(f"x is {x}")



print("\n This program can be shorten and written like this")

while True:
    try:
        z = int(input("What is z? "))
        # Break out of loop if "exception is FALSE"
        break
    except ValueError:
        print("z is not an integer")
 
print(f'"z" is {z}')
            

print("\n This program can be written and shorten with ABSTRACTION")



def main():
    a = get_int()
    print(f"a is {a}")


def get_int():
    while True:
        try:
            # a = int(input("What is a? "))
            # return a
            return int(input("What is a? "))
        except ValueError:
            print('"A" is not an integer')



main()
    

 