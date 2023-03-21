

# BUILT IN ZIP METHOD
def test_zip(x, y):
    t = zip(x,y)
    print(list(t))  
test_zip(["A", "B", "C", "D"],[5, 6, 7, 8])

# The built-in zip function "zips" two lists. Write your own implementation of this function.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.

# First attempt
def zap(a, b):
    new_list = []
    index = 0
    for s in a:
        tup = (s,b[index])
        new_list.append(tup)
        index += 1
    return(new_list)
            
test = zap([0, 1, 2, 3],[5, 6, 7, 8])
print(test)



# BETTER  - Not as ugly but understandable solution
def zap_1(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result
print(zap_1([0, 1, 2, 3],[5, 6, 7, 8]))



# BEST - concise solution with list comprehensions
def zap_2(a, b):
    return [(a[i], b[i]) for i in range(len(a))]
print(zap_2([0, 1, 2, 3],[5, 6, 7, 8]))

