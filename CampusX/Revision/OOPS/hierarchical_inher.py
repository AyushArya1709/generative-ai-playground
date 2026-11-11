class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass


class FeaturePhone(Phone):
    pass


SmartPhone(1000, "Apple", "13px").buy()