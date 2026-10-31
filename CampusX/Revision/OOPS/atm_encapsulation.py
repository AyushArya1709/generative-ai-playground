class ATM:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        print(id(self))

        self.menu()

    # Getter
    def get_pin(self):
        return self.__pin

    # Setter
    def set_pin(self, new_pin):

        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed")

        else:
            print("Not allowed")

    def create_pin(self):
        new_pin = input("Enter your PIN: ")
        self.set_pin(new_pin)

    def deposit(self):

        temp = input("Enter your PIN: ")

        if temp == self.get_pin() and self.__pin != "":

            try:
                amount = int(input("Enter the amount: "))

                if amount > 0:
                    self.__balance += amount
                    print("Deposit successful!")

                else:
                    print("Amount must be greater than zero.")

            except ValueError:
                print("Please enter a valid amount.")

        else:
            print("Invalid PIN or PIN not set.")

    def withdraw(self):

        temp = input("Enter your PIN: ")

        if temp == self.get_pin() and self.__pin != "":

            try:
                amount = int(input("Enter the amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")

                elif amount <= self.__balance:
                    self.__balance -= amount
                    print("Withdrawal successful!")

                else:
                    print("Insufficient balance.")

            except ValueError:
                print("Please enter a valid amount.")

        else:
            print("Invalid PIN or PIN not set.")

    def check_balance(self):

        temp = input("Enter your PIN: ")

        if temp == self.get_pin() and self.__pin != "":
            print("Your balance is:", self.__balance)

        else:
            print("Invalid PIN or PIN not set.")

    def menu(self):

        while True:

            user_input = input("""
Hello, how would you like to proceed?

1. Enter 1 to create/change PIN
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