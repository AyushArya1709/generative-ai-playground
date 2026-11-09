class Parent:

    def __init__(self):
        self.__num = 100

    def show(self):
        print("Parent:", self.__num)


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        print("Child:", self.__var)


dad = Parent()
dad.show()

son = Child()
son.show()