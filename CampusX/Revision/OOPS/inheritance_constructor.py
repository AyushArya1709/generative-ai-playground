class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
        
        
        
class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 13)