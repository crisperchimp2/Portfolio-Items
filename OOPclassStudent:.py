class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id

    def student_info(self):
        print(f"Student Info: {self.name}, Age: {self.age}, Grade: {self.grade}, ID: {self.student_id}")

def get_student_details():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    student_id = input("Enter student ID: ")
    return name, age, grade, student_id

# Creating student objects using user input
student1_details = get_student_details()
student1 = Student(*student1_details)

student2_details = get_student_details()
student2 = Student(*student2_details)

# Printing student information
student1.student_info()
student2.student_info()