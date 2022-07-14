# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yearDays = 365
yearWeek = 52
yearMonth = 12
life_span_years = 90

age_as_int = int(age)
remainingYears = (life_span_years - age_as_int)
remainingDays = round(remainingYears * 365)
remainingWeeks = round(remainingYears * 52)
remainingMonths = round(remainingYears * 12)

print(f"\nYou have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months left.\n")



