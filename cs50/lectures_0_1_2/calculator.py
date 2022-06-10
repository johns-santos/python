def main():

    z = int(input("What is z? "))
    print("z squared is", square(z))



def square(n):
    return pow(n, 2)


name = input("What is your name? \n") 
   
def hello():
    print(f"Hello, {name}")

hello()
print("\n")

main()