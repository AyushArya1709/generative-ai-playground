# =====================================================
# 1. IMPORTING MODULES
# =====================================================

from abc import ABC, abstractmethod
#    ↑      ↑    ↑
#    |      |    └── Abstract Method Decorator
#    |      └─────── Abstract Base Class
#    └────────────── Python Module


# =====================================================
# 2. ABSTRACT PARENT CLASS
# =====================================================

class Employee(ABC):
#     ↑        ↑
#     |        └── Parent Class (ABC)
#     └─────────── Class Name
#
# OOP CONCEPT: ABSTRACTION


    # CLASS VARIABLE / CLASS ATTRIBUTE
    company = "Google"


    # CONSTRUCTOR / INITIALIZER
    def __init__(self, name, salary):
    #   ↑       ↑       ↑     ↑
    #   |       |       |     └── Parameter 2
    #   |       |       └──────── Parameter 1
    #   |       └──────────────── Initializer Method
    #   └──────────────────────── Function Definition

        # SELF = CURRENT OBJECT REFERENCE

        self.name = name
        #   ↑       ↑
        #   |       └── Parameter
        #   └────────── Instance Attribute

        self.__salary = salary
        #   ↑  ↑
        #   |  └── Private Attribute (Name Mangling)
        #   └───── Current Object Reference


    # ABSTRACT METHOD
    @abstractmethod
    # ↑ Decorator

    def work(self):
        pass
        # ↑ Empty Placeholder


    # INSTANCE METHOD
    def show_details(self):

        print(f"Name: {self.name}")
        #    ↑     ↑
        #    |     └── Instance Attribute
        #    └──────── F-string

        print(f"Salary: {self.__salary}")


    # GETTER METHOD
    def get_salary(self):
        return self.__salary
        #     ↑
        #     └── Return Statement


    # SETTER METHOD
    def set_salary(self, new_salary):
        #                  ↑
        #                  └── Parameter

        self.__salary = new_salary
        #                  ↑
        #                  └── Parameter Value


    # CLASS METHOD
    @classmethod
    # ↑ Decorator

    def change_company(cls, new_company):
        #             ↑    ↑
        #             |    └── Parameter
        #             └─────── Class Reference

        cls.company = new_company


    # STATIC METHOD
    @staticmethod
    # ↑ Decorator

    def welcome():
        print("Welcome to the company!")


    # MAGIC / DUNDER METHOD
    def __str__(self):
        return f"Employee Name: {self.name}"


# =====================================================
# 3. CHILD CLASS: DEVELOPER
# =====================================================

class Developer(Employee):
#     ↑         ↑
#     |         └── Parent Class
#     └──────────── Child Class
#
# OOP CONCEPT: INHERITANCE
# RELATIONSHIP: IS-A


    # CHILD CLASS CONSTRUCTOR
    def __init__(self, name, salary, language):

        # PARENT CLASS CONSTRUCTOR CALL
        super().__init__(name, salary)
        # ↑       ↑
        # |       └── Parent Initializer
        # └────────── Parent Class Access


        # INSTANCE VARIABLE
        self.language = language


    # METHOD OVERRIDING
    def work(self):
        print(f"{self.name} is coding in {self.language}")


# =====================================================
# 4. CHILD CLASS: DESIGNER
# =====================================================

class Designer(Employee):
#     ↑       ↑
#     |       └── Parent Class
#     └────────── Child Class


    # METHOD OVERRIDING
    def work(self):
        print(f"{self.name} is designing UI/UX")


# =====================================================
# 5. COMPOSITION
# =====================================================

class Laptop:

    # CONSTRUCTOR
    def __init__(self, brand):

        # INSTANCE VARIABLE
        self.brand = brand


class Programmer:

    # CONSTRUCTOR
    def __init__(self, name, laptop):

        # INSTANCE VARIABLE
        self.name = name

        # COMPOSITION / HAS-A RELATIONSHIP
        self.laptop = laptop


    # INSTANCE METHOD
    def show_laptop(self):
        print(f"{self.name} uses {self.laptop.brand}")


# =====================================================
# 6. OBJECT CREATION / INSTANTIATION
# =====================================================

dev1 = Developer("Ayush", 50000, "Python")
# ↑       ↑           ↑        ↑       ↑
# |       |           |        |       └── Argument 3
# |       |           |        └────────── Argument 2
# |       |           └─────────────────── Argument 1
# |       └─────────────────────────────── Class Instantiation
# └─────────────────────────────────────── OBJECT REFERENCE
#
# Actual Object: Developer instance
# OOP CONCEPT: INSTANTIATION


designer1 = Designer("Rahul", 45000)
# ↑          ↑         ↑        ↑
# |          |         |        └── Argument 2
# |          |         └─────────── Argument 1
# |          └───────────────────── Class Instantiation
# └──────────────────────────────── OBJECT REFERENCE


laptop1 = Laptop("ASUS")
# ↑        ↑       ↑
# |        |       └── Argument
# |        └────────── Class Instantiation
# └─────────────────── OBJECT REFERENCE


programmer1 = Programmer("Ayush", laptop1)
# ↑             ↑          ↑        ↑
# |             |          |        └── Argument (Object)
# |             |          └─────────── Argument (String)
# |             └────────────────────── Class Instantiation
# └──────────────────────────────────── OBJECT REFERENCE


# =====================================================
# 7. ACCESSING INSTANCE ATTRIBUTES
# =====================================================

print(dev1.name)
#     ↑    ↑
#     |    └── Instance Attribute
#     └─────── Object Reference

print(dev1.language)
#     ↑    ↑
#     |    └── Instance Attribute
#     └─────── Object Reference


# =====================================================
# 8. ACCESSING CLASS VARIABLE
# =====================================================

print(dev1.company)
#     ↑    ↑
#     |    └── Class Attribute
#     └─────── Object Reference


# =====================================================
# 9. METHOD CALLING
# =====================================================

dev1.work()
# ↑    ↑
# |    └── Instance Method Call
# └─────── Object Reference

designer1.work()
# ↑          ↑
# |          └── Instance Method Call
# └───────────── Object Reference

dev1.show_details()
# ↑    └── Instance Method Call
# └─────── Object Reference


# =====================================================
# 10. GETTER AND SETTER
# =====================================================

print(dev1.get_salary())
#     ↑    └── Getter Method Call
#     └─────── Object Reference

dev1.set_salary(60000)
# ↑    ↑          ↑
# |    |          └── Argument
# |    └───────────── Setter Method Call
# └────────────────── Object Reference

print(dev1.get_salary())


# =====================================================
# 11. CLASS METHOD CALLING
# =====================================================

Employee.change_company("OpenAI")
# ↑        ↑                ↑
# |        |                └── Argument
# |        └─────────────────── Class Method Call
# └──────────────────────────── Class Reference

print(dev1.company)


# =====================================================
# 12. STATIC METHOD CALLING
# =====================================================

Employee.welcome()
# ↑        ↑
# |        └── Static Method Call
# └─────────── Class Reference


# =====================================================
# 13. MAGIC METHOD CALLING
# =====================================================

print(dev1)
#     ↑
#     └── Object Reference
#
# Python internally calls dev1.__str__()