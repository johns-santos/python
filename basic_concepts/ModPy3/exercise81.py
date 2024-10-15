# 1. Define a base class "Character" that has the following properties:
# name  - String
# hp  - an Integer value representing health (aka hitpoints)
# level  - an integer value representing experience level

# 2. Define a subclass "NPC" (which stands for Non-Player Character) that inherits from Character , and has an additional instance method called speak  which prints the speech that character would say when a player interacts with them. 

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

        
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
    
    def speak(self):
        return f"Hello, my my name is {self.name}."
          

x = NPC("John", 2, 10)
print(x.speak())
print(x.level)

    