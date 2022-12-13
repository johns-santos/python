def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove dolloar sign
    remove_dollar_sign = d.replace("$", "")
    # convert to float and return
    return float(remove_dollar_sign)
  


def percent_to_float(p):
    # Remove percent sign
    remove_percent_sign = p.replace("%", "")
    # Convert to float and divide by 100 for tip amount
    convert_to_tip = float(remove_percent_sign) / 100
    return convert_to_tip
    
    
main()