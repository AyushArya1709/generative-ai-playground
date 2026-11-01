class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating two separate objects
cust1 = Customer("Ayush", 23)
cust2 = Customer("Kanika", 22)


# Assigning cust2 to cust1
cust1 = cust2


# Modifying the object through cust2
cust2.name = "Rahul"


# Printing values
print(cust1.name)
print(cust2.name)

#Id will remain the same

print(id(cust1))
print(id(cust2))