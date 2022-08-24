


spam = ['rats', 'bats', 'mice','dogs','cats']

for i in spam:
    print(i)

# remove method - can be used to remove value in list
spam.remove('rats')
print(spam)
# del method will remove item by index not value
del spam[0]

# append method - used to append value to list
spam.append('rats')
print(spam)
spam.append('bats')

# sort method - used to put values in asci-betical order
spam.sort()
print(spam)

for i in spam:
    print(i.title())

