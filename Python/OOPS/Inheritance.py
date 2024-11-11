# Inheritance is one of the core concepts of object-oriented programming (OOP) that allows a class to inherit properties 
# and behaviors (methods and attributes) from another class. 
# # It helps in creating a hierarchical classification and enables code reusability and polymorphism.

# Key Concepts of Inheritance
# Base Class (Parent or Superclass): The class whose properties and methods are inherited by another class.
# Derived Class (Child or Subclass): The class that inherits from the base class and can add its own properties and methods.
# Reusability: Inheritance allows the reuse of code by creating a new class that is based on an existing class.
# Polymorphism: A child class can have its own implementation of a method, allowing the same method name to behave differently.
class A:
    def __init__(self):
        print("A Class Constructor")
    
    def show(self):
        print("A Method")

class B(A):
    def __init__(self):
        super().__init__()
        print("B Class Constructor")
    def show(self):
        print("B Class")

b1 = B()
# b1.show()
# print(B.__mro__)