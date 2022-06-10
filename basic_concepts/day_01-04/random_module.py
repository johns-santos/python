from cgi import test
import random

test_array = ['car', 'red', 'candy', 'skunk']
random_integer = random.randint(0, len(test_array)-1)


print(test_array[random_integer])

random_float = random.random()# This will run between 0 and 1 but not including 1 (0.00000000 - 0.999999999....)
print(random_float)

# Expand and go beyound 0-1 (multiply by upper limit number)
random_float_to_Int = random.random()*5 # returns 0.00000 - 4.999999....
print(random_float_to_Int)