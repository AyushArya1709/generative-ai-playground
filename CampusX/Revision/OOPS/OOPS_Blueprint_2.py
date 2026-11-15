# ==========================================
# 1. CLASS
# ==========================================

class Student:
    # Student = CLASS NAME

    college = "CHRIST University"
    # CLASS VARIABLE / CLASS ATTRIBUTE


    # ======================================
    # 2. CONSTRUCTOR
    # ======================================

    def __init__(self, name, age):
        # __init__ = CONSTRUCTOR / INITIALIZER
        # self     = CURRENT OBJECT REFERENCE
        # name     = PARAMETER 1
        # age      = PARAMETER 2

        self.name = name
        # self.name = INSTANCE VARIABLE / ATTRIBUTE
        # name      = PARAMETER

        self.age = age
        # INSTANCE VARIABLE / ATTRIBUTE


    # ======================================
    # 3. INSTANCE METHOD
    # ======================================

    def show_details(self):
        # show_details = INSTANCE METHOD
        # self         = CURRENT OBJECT REFERENCE

        print(self.name)
        print(self.age)


    # ======================================
    # 4. CLASS METHOD
    # ======================================

    @classmethod
    # DECORATOR: Converts method into a class method

    def change_college(cls, new_college):
        # cls         = CLASS REFERENCE
        # new_college = PARAMETER

        cls.college = new_college


    # ======================================
    # 5. STATIC METHOD
    # ======================================

    @staticmethod
    # DECORATOR: Creates a static method

    def welcome():
        print("Welcome to Student Portal!")


# ==========================================
# 6. OBJECT CREATION / INSTANTIATION
# ==========================================

student1 = Student("Ayush", 23)
# ↑          ↑       ↑        ↑
# |          |       |        └── ARGUMENT 2
# |          |       └─────────── ARGUMENT 1
# |          └─────────────────── CLASS INSTANTIATION
# └────────────────────────────── OBJECT REFERENCE
#
# Actual result = OBJECT


# ==========================================
# 7. ATTRIBUTE ACCESS
# ==========================================

print(student1.name)
# student1 = OBJECT REFERENCE
# .        = ATTRIBUTE ACCESS OPERATOR
# name     = INSTANCE ATTRIBUTE


print(student1.college)
# college = CLASS ATTRIBUTE


# ==========================================
# 8. METHOD CALLING
# ==========================================

student1.show_details()
# show_details() = INSTANCE METHOD CALL


# ==========================================
# 9. CLASS METHOD CALLING
# ==========================================

Student.change_college("OpenAI University")
# Student        = CLASS
# change_college = CLASS METHOD
# Argument       = "OpenAI University"


# ==========================================
# 10. STATIC METHOD CALLING
# ==========================================

Student.welcome()
# welcome() = STATIC METHOD CALL


# ==========================================
# 11. INHERITANCE
# ==========================================

class GraduateStudent(Student):
    # GraduateStudent = CHILD CLASS
    # Student         = PARENT CLASS
    # Concept         = INHERITANCE
    # Relationship    = IS-A

    def __init__(self, name, age, degree):
        # CHILD CLASS CONSTRUCTOR

        super().__init__(name, age)
        # super() = ACCESS PARENT CLASS
        # __init__() = PARENT INITIALIZER

        self.degree = degree
        # INSTANCE ATTRIBUTE


    # ======================================
    # 12. METHOD OVERRIDING
    # ======================================

    def show_details(self):
        # METHOD OVERRIDING
        # Same method name, new implementation

        print(self.name)
        print(self.age)
        print(self.degree)


# ==========================================
# 13. CHILD CLASS OBJECT
# ==========================================

student2 = GraduateStudent("Rahul", 24, "Data Science")
# ↑           ↑                   ↑       ↑     ↑
# |           |                   |       |     └── ARGUMENT 3
# |           |                   |       └──────── ARGUMENT 2
# |           |                   └──────────────── ARGUMENT 1
# |           └──────────────────────────────────── CLASS
# └──────────────────────────────────────────────── OBJECT REFERENCE


# ==========================================
# 14. POLYMORPHISM
# ==========================================

student1.show_details()
student2.show_details()
# Same method call, different implementations
# CONCEPT = POLYMORPHISM