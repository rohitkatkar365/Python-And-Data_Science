# ## Exercise: Inheritance

# 1. create inheritance using animal Dog relation.
# ```
# for example, 
#     Animal and Dog both has same habitat so create a method for habitat 
# ```

# 2. use super() constructor for calling parent constructor.

# ```
# class Animal:
#     #code

# class Dog(Animal):
#     super()-it refers Animal class,now you can call Animal's methods.
# ```

class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def show_habitat(self):
        print(f"Habitat: {self.habitat}")

class Dog(Animal):
    def __init__(self, habitat, name):
        super().__init__(habitat)  # Calling the parent class constructor
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")
        self.show_habitat()  # Calling the method from the parent class

# Creating an instance of Dog
dog = Dog("Domestic", "Buddy")

# Displaying information
dog.show_info()

        

