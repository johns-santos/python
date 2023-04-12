f1 = open("file1.txt")
res1 = []
for i in f1:
    res1.append(int(i.strip('\n')))

f2 = open("file2.txt")
res2 = []
for i in f2:
    res2.append(int(i.strip('\n')))

# List of items found in both files
res3 = []
res3 = [item for item in res1 if item in res2] # Create new item list
print(res3)

print(" ")

# LIST OF ITEMS found in one of the files
res4 = []
res4 = [item for item in res1 if item not in res2] # Create new item list
print(res4)   