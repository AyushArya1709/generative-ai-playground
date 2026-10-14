from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    cgpa: float

# Student 1
student1: Student = {
    "name": "Ayush",
    "age": 23,          
    "cgpa": 6.82
}

# Student 2
student2: Student = {
    "name": "Riya",
    "age": 21,
    "cgpa": 8.45
}

# Student 3
student3: Student = {
    "name": "Karan",
    "age": 22,
    "cgpa": 7.10
}

# Student 4
student4: Student = {
    "name": "Meera",
    "age": 20,
    "cgpa": 9.05
}

# Print all of them
students = [student1, student2, student3, student4]

for i, s in enumerate(students, start=1):
    print(f"Student {i}: {s}")
