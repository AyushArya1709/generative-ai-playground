class Student:

    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Ayush", "Data Science", 85)

student1.display_info()
student1.check_result()

