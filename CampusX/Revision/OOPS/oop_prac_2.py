class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        temp_num = other.den * self.num + self.den * other.num 
        temp_den = self.den * other.den
        
        return "{}/{}".format(temp_num,temp_den)
    
x = Fraction(4,5)
y = Fraction(3,6)

print(x + y)
