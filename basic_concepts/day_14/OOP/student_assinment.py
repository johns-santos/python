# stopped at 2:12


import random

## *********** FACTORY CLASS METHOD  **********  
## Class method to create instantiate multiple objects (factory for multiple)
## *************************************************** 
class Selector:
    def __init__(self):
        self.schools = ["EHS", "TJHS", "FTHS", "MSH"]
    
    def sort(self, name):
        print(name, "will enroll at ", random.choice(self.schools))
       
school = Selector()
school.sort("Isabella") 


## *********** SINGLE INSTANCE CLASS METHOD **********         
# ######## Class method for ONE "singulton" instance.  ######
## ***************************************************    
class Selector01:
    schools = ["EHS", "TJHS", "FTHS", "MSH"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is enrolled at ", random.choice(cls.schools))
      
Selector01.sort("John")   
