# Class is a OBJECT - It is a data type
class Student:
     # Clas can have a function called a METHOD.
     # "__init__" function INSTANCIATES the OBJECT (Stores in memory)
    def __init__(self, name, school):
         # Check attributes and catch errors with "raise"
         if not name:
             raise ValueError("Missing Name.")
         if school not in ["EHS", "TJHS", "FTHS"]:
             raise ValueError("Invalid school")
         # Declare INSTANCE variables
         self.name = name
         self.school = school     
    # Object method "__str__" returns class or attributes as a strings   
    def __str__(self):
        return f"{self.name} from {self.school}"
    
def main():
    student = get_student()
    print(student)
  
def get_student():
    name = input("Name: ")
    school = input("School: ")
    # Construct the object - attributes are added by ("__init__")
    return Student(name, school)
    
if __name__ == "__main__":
    main()