class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def create_pin(self):
        self.pin = input("Enter your PIN: ")
        print("PIN set successfully!")

    def deposit(self):
        temp = input("Enter your PIN: ")

        if temp == self.pin and self.pin != "":
            amount = int(input("Enter the amount: "))

            if amount > 0:
                self.balance += amount
                print("Deposit successful!")
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid PIN or PIN not set.")

    def withdraw(self):
        
        temp = input("Enter your PIN: ")
        if temp == self.pin and self.pin != "":
            amount = int(input("Enter the amount: "))
            
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount <= self.balance:
                self.balance -= amount
                print("Withdrawl successful")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid pin or PIN not set.")
            
    def check_balance(self):
        temp = input("Enter your PIN: ")

        if temp == self.pin and self.pin != "":
            print("Your balance is:", self.balance)
        else:
            print("Invalid PIN or PIN not set.")

    def menu(self):
        while True:
            user_input = input("""
Hello, how would you like to proceed?

1. Enter 1 to create PIN
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit

Enter your choice: """)

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.deposit()

            elif user_input == "3":
                self.withdraw()

            elif user_input == "4":
                self.check_balance()

            elif user_input == "5":
                print("Bye!")
                break

            else:
                print("Invalid input. Please try again.")


obj = ATM()
