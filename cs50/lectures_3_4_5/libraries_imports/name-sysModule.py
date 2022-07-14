###########################
#  sys module allows program to accept arguements provided by user
###########################
# sys.ext - forces the program to exit if condition is met

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguements.")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguements")

# print("Hello, my name is", sys.argv[1]+".")

###### Shorten code above with a loop ######

####### Slice the list to start at location 1 of list --
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
 



