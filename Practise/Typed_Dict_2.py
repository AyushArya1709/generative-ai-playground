from typing import TypedDict

class Employee(TypedDict):
    name: str
    skills: list[str]
    experience: int

employee1: Employee = {
    "name": "Aarav",
    "skills": ["Singing", "Dancing", "Jumping"],
    "experience": 10,
}

employee2: Employee = {
    "name": "Priya",
    "skills": ["Communication", "Negotiation", "Public Speaking"],
    "experience": 5,
}

employee3: Employee = {
    "name": "Meera",
    "skills": ["Data Analysis", "Project Management"],
    "experience": 45,
}

Employees = [employee1, employee2, employee3]

for i, e in enumerate(Employees, start=1):
    skills = ", ".join(e["skills"])
    print(f"Employee {i}: {e['name']} | Skills: {skills} | Experience: {e['experience']} yrs")
