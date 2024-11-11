# Operator Overloading in Python allows you to define how built-in operators like +, -, *, and == behave for custom objects. 
# This means you can use operators with objects of your classes, giving them custom behavior based on their types. 
# By overloading operators, you can make your objects more intuitive and easier to work with.

class Complex:
    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2
    
    def __add__(self,other):
        c1 = self.c1 + other.c1
        c2 = self.c2 + other.c2
        s3 = Complex(c1,c2)
        return s3
    
    def __str__(self):
            return f"{self.c1} + {self.c2}i"


c1 = Complex(1,2)
c2 = Complex(2,3)
print(c1+c2)