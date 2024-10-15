class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"You want {key}? Well it aint here!")
        
    def __setitem__(self, key, value):
        print("YOu want to change dictioary?")
        print("Okay fine.")
        super().__setitem__(key, value)
        
    def __contains__(self, item):
        # Just an example... will return no for all
        print("No it aint in here!!!")
        return False
    
    
# Create a key pair dictionary with GrumpyDict.  b 
data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)


data['city'] = 'Tokyo'
print(data)
'city' in data