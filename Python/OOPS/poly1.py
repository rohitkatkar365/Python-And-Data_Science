# Poly means "many," and morph means "forms." So, polymorphism means "many forms."
# Function Overloading: Multiple functions with the same name but different parameters.
# Method Overriding: A child class provides a specific implementation of a method that is already defined in its parent class.
# Duck Typing: In Python, if an object behaves like a certain type (i.e., it has the required methods or attributes), it can be treated as that type, regardless of its actual class.

# Types of Polymorphism in Python
# Compile-Time Polymorphism (Function Overloading): Achieved through multiple functions with the same name but different parameters. Python doesn’t support function overloading directly but can be emulated using default arguments.
# Run-Time Polymorphism (Method Overriding): Achieved through inheritance, where the child class overrides a method of its parent class.

# Advantages of Polymorphism
# Code Reusability: Allows functions and methods to use objects of different classes interchangeably.
# Flexibility: Enables writing more flexible and generalized code.
# Simplified Code Maintenance: Reduces the complexity of the code, making it easier to maintain and extend.

# Run-time polymorphism

class A:
    def __init__(self):
        print("A Class Constructor")
    
    def show(self):
        print("A Method")
    # support but this not better way(if not parameter pass)
    # def show(self,a):
    #     print("nddnfjmdf"+self.a)

class B(A):
    def __init__(self):
        super().__init__()
        print("B Class Constructor")
    def show(self):
        print("B Class")

class C(B):
    def __init__(self):
        super().__init__()
        print("B Class Constructor")
    def show(a):
        print("C Class")

a1 = A()
a1.show(1)
c1 = C()
c1.show()
print(C.__mro__)