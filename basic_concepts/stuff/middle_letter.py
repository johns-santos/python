def mid(s):
    if len(s) % 2 == 0:
        return("")
    else:
        x = int(len(s)/2)
        return(s[x])

    
test = mid("abc")
print(test)