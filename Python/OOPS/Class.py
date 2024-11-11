# A class in Python defines a new data type that can have attributes (variables) and methods (functions).

class Computer:
    # Behavior defined in class that is called "method"
    def config(self):
        print("I5 8GB 1TB")

# An entity that has state and behavior is known as an "object" 

# First Way
Computer.config(Computer)

# Second Way
comp1 = Computer()
comp1.config()

# Third Way
Computer.config(comp1)