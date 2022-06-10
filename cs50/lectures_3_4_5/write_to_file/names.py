
# ====== This is lost after executed ============
names = []

for _ in range(3):
    # Prompt user 3 times for a name and add to list
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"hello, {name}")
# ====================================
print("\n")





# ====== WRITE to file with 'open'
# ============================================
name1 = input("\nWhat is your name? \n")
#1) save name1 output to file with 'open'
#2) use "a" option to APPEMD to file
#3) use "with as file" to close file after automatically
with open("names.txt", "a") as file:
    file.write(f"{name1}\n")


print("\n")


# ===== READ a file ========
# ============================================
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip()) # Use rstrip to remove lines printed by print


print("\n SORTED ALPHABETICALLY \n")
# READ and SORT data from file
names2 = []

with open("names.txt") as file:
    for line in file:
        names2.append(line.rstrip())

for item in sorted(names2, reverse=True):
    print(f"hello, {item}")



