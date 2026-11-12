'''
class Geometry:
    
    def area(self, a, b = 0):
        if b == 0:
            print("Circle", 3.14 * a * a)
        else:
            print("Rectangle", a * b)
    
obj = Geometry()
obj.area(4)
obj.area(4,5)
'''
from fractions import Fraction

class Geometry:
    
    def area(self, r, h):
        return Fraction(1, 3) * Fraction(22, 7) * r * r * h
    
obj = Geometry()
print(obj.area(5,4))