
# 
# Class method example - Instantiate student object using the class method


class Student:
    def __init__(self, name, school):
         self.name = name
         self.school = school  
             
    def __str__(self):
        return f"{self.name} from {self.school}"
    
    # ###########  Create a class method ###############
    @classmethod
    def get(cls):
        name = input("Name: ")
        school = input("School: ")
        return cls(name, school)
    
def main():
    # Call the "get" method in the Student class
    student = Student.get()
    print(student)
    

if __name__ == "__main__":
    main()
  

