# Compare each item in list to one another

# def all_equal(list):
#     for s in list:
#         if s != list[0]:
#             return False
#     return True

def all_equal(list):
    for s in list:
        for i in list:
            print(f"{s} : {i}")
            if s != i:
                return False
    return True
        
          
test = all_equal([1,2,3])
test2 = all_equal([5,5,5])
test3 = all_equal(["s", "s", "s", "s"])
test4 = all_equal([4,5,4,4,4,4,4])

print(test)
print(test2)
print(test3)
print(test4)