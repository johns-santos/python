


names = ["bruno", "zoey", "bob", "tom", "jack", "zeke", "bella", "john"]
nick_names = ["jack", "bob", "ali", "luke", "tom", "jim"]
redudant_names = []

for i in names:
    print(i)


print("\n Second List")

for i in names:
    if i in nick_names:
        redudant_names.append(i)
    
print(redudant_names)
        