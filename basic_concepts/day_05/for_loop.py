


# RANGE is objects starting at first arguement and ending before second arguement
for n in range(1, 20):
    print(n)


# Write program that calculates the sum of all even numbers from 1 and 100. Include 1 and 100. This solution adds all even numbers between 1 and 100 adds them to a list, then returns the sum of items.
newList = []
for number in range(1, 101):
    if number % 2 == 0:
        newList.append(number)
print(sum(newList))


print("\n")


# Use range to count by a specified number. Example below - start at 1 and count by 4 to 100.
for i in range(1, 101, 4):
    print(i)


print("\n")


# Use range to count by a specified number. Example below - start at 2 and count by 2 to 100 and add all nureturned numbers.
sum = 0
for i in range(2, 101, 2):
    sum = i + sum
print(sum)
   

        

    


