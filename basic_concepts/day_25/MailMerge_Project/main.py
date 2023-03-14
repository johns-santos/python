PLACEHOLDER = "[name]"


# Read file containing names and make a list
with open("./Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()

# Open and read email template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    # Replace the string "[name]" with the name of each name in list
    for name in name_list:
        # Remove space
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
       
       # Create a new file in specified locatino and write new letter to file
        with open(f"./Output/ReadyToSend/my_file_{stripped_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)
        