class A:
    def m1(self):
        return 20


class B(A):
    def m1(self):
        # Calling the parent class (A) method using super()
        val = super().m1() + 30
        return val


class C(B):
    def m1(self):
        # Intentional recursion: calling the same method repeatedly
        val = self.m1() + 20

        # Alternative: Call the parent class (B) method using super()
        # val = super().m1() + 20

        return val


# Creating an object of class C
obj = C()

# Calling m1() will cause infinite recursion
# because self.m1() repeatedly calls C's own m1() method.
print(obj.m1())