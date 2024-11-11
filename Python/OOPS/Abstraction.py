# Abstraction nothing but partial implementation

# Benefits of Abstraction
# Modularity: Code can be divided into smaller parts, making it easier to manage and modify.
# Reusability: Abstract classes provide a template for other classes, promoting code reusability.
# Improved Code Organization: Abstraction helps organize code by separating what a class does from how it does it.
# Ease of Maintenance: Changes to implementation details don’t affect the interface, making maintenance easier.

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(ABC):
    def leg(self):
        print("4")

class Dog(Animal,Cow):
    def sound(self):
        print("Bohw")


c1 = Cat()
c1.sound()
# c2 = Cow()
# c2.leg()
c3 = Dog()
c3.sound()
c3.leg()

