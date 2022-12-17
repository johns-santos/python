import pprint


message = 'It was a bright could day in April, and the clocks were striking thirteen.'
message = message.upper()
count = {}

# Use a for loop to iterate over every character in the 'message' varable. Adding character to dict
for character in message:
# If character does not exit in count, then create the key and set the default value zero(0)
    count.setdefault(character, 0)
# If the character key does exist, then add 1 to  value.
    count[character] = count[character] + 1


## pprint will print out dictionary in column and sorted in order. Making it easier to read.
pprint.pprint(count)

print("")

