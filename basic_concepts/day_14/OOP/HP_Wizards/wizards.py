# Inheritance

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
       
        
class Student(Wizard):
    def __init__(self, name, house):
        # Call Wizard "Super" class
        super().__init__(name)
        self.house = house
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
        
           
        
student = Student("Harry", "Gryffidnor")
student01 = Student("Ron", "Gryffidnor")
professor = Professor("Severrus", "Defense Against the Dark Arts")
wizard = Wizard("Albus")

print(student.name, student.house, student.patronuse)
print(student01.name, student01.house, student01.patronuse)
print(wizard.name)
print(professor.name, professor.subject, professor.patronuse)
