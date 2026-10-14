from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str
    
new_person: Person = {
    "name": "Soni Sinha",
    "age": 46,
    "email": "soni.sinha@example.com"
}

print(new_person)