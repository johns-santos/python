# Write a function named format_number that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousands separator.

def format_number(pos_num):
    if pos_num > 0:
        converted = format(pos_num, ",")
        #return type(converted)
        return converted
        
test = format_number(3000000)
print(test)