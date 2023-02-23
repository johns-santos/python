# Class OPERATOR OVERLOADING.......

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    ## Combine values of both family vaults
    ## by implementing OPERATOR OVERLOADING "object.__add__(self, other)"
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
  
# Initiliaze and print Potters family vault          
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

cheezy = Vault(45, 70, 90)/new-years-bonus/
print(cheezy)

# Call OPERATOR OVERLOAD method (__add__) to combine two vaults.
total = (potter + weasley + cheezy)
print(total)