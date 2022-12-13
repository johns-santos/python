def main():
    convert()
    test()

def convert():
    userInput = input("")
    print(userInput.replace(":)", "🙂").replace(":(","🙁"))



def test():
    cost = int(150)
    total = (cost * 7.75)
    print(f"{total}")

       
main()