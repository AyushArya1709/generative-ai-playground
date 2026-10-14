from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10)

new_student = {'name': 'Ayush'
               , 'age': 20
               , 'email': 'laudalega@chutiya.com'
               , 'cgpa': 8.5}

student = Student(**new_student)

print(student)
print(type(student))

print(student.name)

student_dict = dict(student)

print(student_dict['cgpa'])

student_json = student.model_dump_json()

print(student_json)