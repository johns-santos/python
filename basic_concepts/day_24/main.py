
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    
with open("my_file_2.txt", "a") as file:
    file.write(f"\nNew Text")


