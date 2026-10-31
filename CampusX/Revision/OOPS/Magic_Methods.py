import math

class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def simplify(self):
       gcd = math.gcd(self.num, self.den)

       self.num //= gcd
       self.den //= gcd

    def __add__(self, other):

        temp_num = other.den * self.num + self.den * other.num
        temp_den = self.den * other.den

        result = Fraction(temp_num, temp_den)
        result.simplify()

        return result

    def __sub__(self, other):

        temp_num = other.den * self.num - self.den * other.num
        temp_den = self.den * other.den

        result = Fraction(temp_num, temp_den)
        result.simplify()

        return result

    def __mul__(self, other):

        temp_num = self.num * other.num
        temp_den = self.den * other.den

        result = Fraction(temp_num, temp_den)
        result.simplify()

        return result

    def __truediv__(self, other):

        temp_num = self.num * other.den
        temp_den = self.den * other.num

        result = Fraction(temp_num, temp_den)
        result.simplify()

        return result


x = Fraction(4,5)
y = Fraction(3,6)

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)