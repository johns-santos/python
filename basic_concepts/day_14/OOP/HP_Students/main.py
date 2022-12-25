
# Class is a OBJECT - It is a data type
class Student:
     # Clas can have a function called a METHOD.
     # "__init__" function INSTANCIATES the OBJECT (Stores in memory)
     def __init__(self, name, house):
         # Declare INSTANCE variables
         self.name = name
         self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}.")

def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    # Construct the object - attributes are added by ("__init__")
    student = Student(name, house)
    return student
    

if __name__ == "__main__":
    main()