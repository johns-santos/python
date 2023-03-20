def only_ints(x,y):
    return(type(x) == int and type(y) == int)
    
s = only_ints(5,4.555)
print(s)