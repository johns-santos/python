
# Class is a OBJECT - It is a data type
class Student:
     # Clas can have a function called a METHOD.
     # "__init__" function INSTANCIATES the OBJECT (Stores in memory)
    def __init__(self, name, school, mascott):
         # Check attributes and catch errors with "raise"
         if not name:
             raise ValueError("Missing Name.")
         if school not in ["EHS", "TJHS", "FTHS"]:
             raise ValueError("Invalid school")
         # Declare INSTANCE variables
         self.name = name
         self.school = school
         self.mascott = mascott
    
    # Object method "__str__" returns class or attributes as a strings   
    def __str__(self):
        return f"{self.name} from {self.school}"
    
    def spirit(self):
        match self.mascott:
            case "bear":
                return "👹"
            case "mustang":
                return "🙊"
            case "buffallo":
                return "😾"
            # CASE for empty input
            case _:
                return ":("
        
    
def main():
    student = get_student()
    print("School Spirit!!!!!!")
    print(student.spirit())

def get_student():
    name = input("Name: ")
    school = input("School: ")
    mascott = input("Mascot: ")
    # Construct the object - attributes are added by ("__init__")
    return Student(name, school, mascott)
    
if __name__ == "__main__":
    main()