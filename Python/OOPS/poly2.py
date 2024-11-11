# Duck-Typing

# Duck typing is a concept related to dynamic typing in Python. It means that the suitability of an object for a 
# particular purpose is determined by the presence of certain methods and properties, rather than the actual type of the object.

class VScode:
    def execute(self):
        print("Compile")
        print("Run")

class PyCharm:
    def execute(self):
        print("Compile")
        print("Run")
        print("Restart")

class Laptop:

    def code(self,ide):
        ide.execute()

# ide = VScode()
ide = PyCharm()
l1 = Laptop()
l1.code(ide)