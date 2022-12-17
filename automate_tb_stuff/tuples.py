# TUPLES - same as list except they are inmutable and use paratheses() instead of brackets{}.

stuff = {'name':'sophie','species':'cat','age':12}

print("")
print(list(stuff.keys()))

for v in stuff.values():
    print(v)
    
print("")
for k in stuff.keys():
    print(k)

### TUPLES - use multiple assignment to print tuple (key, pair)
print("")
for k,v in stuff.items():
    print(f"{k} : {v}")

## TUPLES - use single assignment to return tuple(key, value)
print("")
for i in stuff.items():
    print(i)