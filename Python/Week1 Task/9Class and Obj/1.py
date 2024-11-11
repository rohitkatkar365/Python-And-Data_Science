# ## Exercise: Class and Objects
# 1. Create a sample class named Employee with two attributes id and name 
# ```
# employee :
#     id
#     name
# ```
# object initializes id and name dynamically for every Employee object created.
# ```
# emp = Employee(1, "coder")
# ```
# 2. Use del property to first delete id attribute and then the entire object

class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        print(id,name)
    
emp1 = Employee(1,"Rohit")

del emp1.id
# print(emp1.id) AttributeError: 'Employee' object has no attribute 'id'
del emp1
# print(emp1)   NameError: name 'emp1' is not defined