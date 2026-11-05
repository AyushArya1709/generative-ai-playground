class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


# Without User in Student(User): Just two normal classes minding their own business.
# Add User to the parentheses: BOOM! Inheritance unlocked. 🤣
# One word changed, and Student got a free upgrade!

class Student(User):

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")


stu1 = Student()

stu1.enroll()
stu1.review()

stu1.login()
stu1.register()