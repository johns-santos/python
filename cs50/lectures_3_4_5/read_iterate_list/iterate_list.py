from xml.etree.ElementInclude import include


list1 = ['texas', 'missippi', 'ohio', 'austin', 'dallas', 'philly', 'new your', 'chicago', 'california']

list2 = ['texas', 'missippi', 'ohio', 'austin', 'dallas', 'chicago', 'california']

list3 = []


print("\n== Iterate over items=====\n")
for item in list1:
    if item not in list2:
        list3.append(item)


print(list3)
print("\n")


print("\n == Use LIST function to Create new unnamed or saved list")
diff_list = list(set(list1) - set(list2))
print(diff_list)



print("\n == Use LIST to create new list")
x = list(('apple', 'banana', 'cherry'))
print(x)
print(type(x))