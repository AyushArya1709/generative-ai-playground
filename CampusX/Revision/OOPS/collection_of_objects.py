class Customer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def intro(self):
        print("I am", self.name, "and I am", self.age)
        
c1 = Customer("Ayush", 23)
c2 = Customer("Ankita", 28)
c3 = Customer("Raghav", 27)

L1 = [c1,c2,c3]

for i in L1:
    i.intro() 