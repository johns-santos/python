
# For loop
numbers = [1,2,3]
new_list = []
for n in numbers:
    new_num = n + 1
    new_list.append(new_num)
print(new_list)


# List comprehsion - list code than FOR LooP
# new_list = [Do_something_to_item for item in old_list]
numbers_2 = [1,2,3]
new_list_2 = []
new_list_2 = [n + 1 for n in numbers_2]
print(new_list_2)

numbers_3 = [1,3,4]
new_list_3 =[item + 1 for item in numbers_3]
print(new_list_3)


# OLD WAY
range_list = []
for num in range(1,5):
    range_list.append(num*2)
print(range_list)

# List Comprehension way - more precise
range_list_2 = [num * 2 for num in range(1,5)]
print(range_list_2)


# CONDITIONAL list comprehension
# EXAMPLE - new_list_5 = [new_item for item in list if test ]
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elaanor', 'Freddie']
short_name = [name for name in names if len(name) <= 4]
print(short_name)

# CONDITIONAL + List Comprehension (Create new item and add to list if len greater than 5)
upper_case_names = [name.upper() for name in names if len(name) > 5]
print(upper_case_names)









def flatten(nestedlist):
    flatlist=[]
    for sublist in nestedlist:
        for element in sublist:
            flatlist.append(element)
    return flatlist
print(flatten([[1, 2], [3, 4], [5,6,7,8,9,10]]))


def combined_list(multi_list):
    long_list = []
    for lst in multi_list:
        for item in lst:
            long_list.append(item)
    return long_list
print(combined_list([[1, 2], [3, 4], [5,6,7,8,9,10]]))




    