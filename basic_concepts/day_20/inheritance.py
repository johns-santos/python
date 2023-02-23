# Inheritate alls subclass to inheritate all methods and attributes of SUPER CLASS


class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")
        
        
# Allow Fish to INHERITATE Animal class methods and attributes
class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    # Inheritate method from super class and add to it    
    def breathe(self):
        super().breathe()
        print("Doing this underwater")
    
    def swim(self):
        print("Moving through water.")
        
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)