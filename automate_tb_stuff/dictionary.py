

myCat = [{'id':'0', 'ownerName':'John Santos','catName':'Zophie', 'species': 'cat', 'age':8, 'size':'large'}, {'id':'1','ownerName':'Isabella Santos','catName':'Midnight', 'species': 'cat', 'age':12, 'size':'medium'}]


print(f"My cat {myCat[0]['catName']} is {myCat[0]['age']} years old.")
print(f"My cat {myCat[1]['catName']} is a {myCat[1]['size']} size cat.")

def findMatch(name):
    res = None
    for match in myCat:
        if match['ownerName'] == name:
            res = match
            #return str(res['id'])
            return res['id']
            break

print(findMatch('Isabella Santos'))
print(myCat[1])


print("")


