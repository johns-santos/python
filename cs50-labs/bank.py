def main():
    greeting = input("Greeting: ").lower().strip()
    banks_money = cash_amount(greeting)
    print(f"${banks_money}")


def cash_amount(greeting):
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

main()