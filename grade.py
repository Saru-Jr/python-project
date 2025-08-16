class student:
    def __init__(self, name, class_name, grade):
        self.name = name
        self.grade = grade
        self.class_name = class_name

    def get_status(self):
        if self.grade > 40 and self.grade <= 50:
            return 'Grade: D'
        elif self.grade > 50 and self.grade <= 60:
            return 'Grade: C'
        elif self.grade > 60 and self.grade <= 75:
            return 'Grade: B'
        elif self.grade > 75 and self.grade <= 100:
            return 'Grade: A'
        elif self.grade > 100:
            return 'Grade: invalid'
        else:
            return 'Grade: F'
    
    def __str__(self):
        return f"Name: {self.name}, Class: {self.class_name}, {self.get_status()}"
    
name = input("Enter your name: ")
class_name = input("Enter your class name: ")
grade = float(input("Enter your grade: "))

student = student(name, class_name, grade)
print(student)