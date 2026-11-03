class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def greet(customer):
    if customer.gender == "male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "ma'am")

    return customer


# Main code

cust = Customer("Ayush", "male")

greet(cust)

cust2 = Customer("Kanika", "female")

new_cust = greet(cust2)

print(new_cust.name)