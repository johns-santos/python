# Add GETTERS and SETTERs. Compare this file to main.py
# Using GETTER and SETTER for ERROR CHECKING
class Student:
    def __init__(self, name, school):
         self.name = name
         self.school = school  
             
    def __str__(self):
        return f"{self.name} from {self.school}"
    
    # GETTER ****** GETTER identified by "@property" ****** 
    @property
    def school(self):
        # Underscore represents "variable" as to not collide with "school" property.
        return self._school
    
    # SETTER ****** SETTER identified by "@school.setter" ****** 
    @school.setter
    def school(self, school):
        if school not in ["EHS", "TJHS", "FTHS"]:
             raise ValueError("Invalid school")
         # Underscore represents "variable" as to not collide with "school" property.
        self._school = school
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name.")
        self._name = name


def main():
    student = get_student()
    # FOLLOWING reassignment is not ALLOWED by SETTER 
    # student.school = "Sammy, Funny Man"
    print(student)
  


    
  
def get_student():
    name = input("Name: ")
    school = input("School: ")
    return Student(name, school)
    
if __name__ == "__main__":
    main()