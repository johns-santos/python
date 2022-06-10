from typing import final


print("\nWelcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = int(input("\nWhat percentage tip would you like to give? 10, 15, or 20?\n"))
people = int(input("How many people to split the bill\n"))


tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = round((bill + total_tip_amount),2)
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)
total_bill = "{:.2f}".format(total_bill)

print(f"\nEach person shoudl pay:  \n ${final_amount} for a total of ${total_bill}\n")