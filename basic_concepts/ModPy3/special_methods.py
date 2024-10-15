# These methods use dunder (__*__) and are consider magic emthods
# Python Magic methods are the methods starting and ending with d
# ouble underscores ‘__’. They are defined by built-in classes in 
# Python and commonly used for operator overloading. 
from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    # DUNDER methods below
    def __repr__(self):
        # Instead of this <__main__.Human object at 0x7fe0d29b3d90>
        return f"Human named {self.first} {self.last}, aged {self.age}"
    def __len__(self):
        return self.age
    # Funny example below -- adding two objects - similiar to concating strings
    def __add__(self, other):  
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return f"You can not do that"
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Cant multiply"
    
    
    
    
class Cat:
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age



j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)

print(j)
print(len(j))
print(j+k)

print("")
o = Cat("Street", "black",2) 
print(j+o)


print("")
print(j*2)

triplets = j * 3
triplets[1].first = 'Jessica'
triplets[2].first = 'Janet'
print(triplets)

print("")
triplets2 = (k + j) * 3
print(triplets2)
