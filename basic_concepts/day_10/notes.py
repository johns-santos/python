# ----- FUNCTION with RETURN


def format_name(f_name, l_name):
    formated_name = (f"{f_name} {l_name}").title()
    return formated_name

# Variable to hold unformated name
formated_string = format_name("john", "santos")
# Print formated name
print(formated_string)



# Accept user input and return formated name
print(format_name(input("What is your first name? "), input("What is your last name? ")))


print("\n")

# Add if statement to handle unxepcted input
def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Invalid user input. Please enter first and last name."
    formated_name2 = (f"{f_name} {l_name}").title()
    return formated_name2

# Accept user input and return formated name
print(format_name2(input("What is your first name? "), input("What is your last name? ")))