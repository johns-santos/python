# https://video.cs50.io/TJKnZ784bSI?start=8725
# NOTES - up to 2:33

def main():

    # Define a function with a default parameter of 'to' with default arguement of 'world'
    def hello(to="world"):
        print("\nHello,", to)

    # Create a varialble with user input 
    name = input("What is your name:\n ")

    # Call "hello" function  with 'name' as the arguement - using the input
    hello(name)

    # Call "hello" with default parameter
    hello()

# Execute main to call defined functions
main()





