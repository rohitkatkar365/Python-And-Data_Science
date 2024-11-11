# Multiple inheritance

class A:
    def __init__(self):
        print("A Class Constructor")
    
    # def show(self):
    #     print("A Method")

class B:
    def __init__(self):
        super().__init__()
        print("B Class Constructor")
    def show(self):
        print("B Class")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("B Class Constructor")
    # def show(a):
    #     print("C Class")

c1 = C()
c1.show()
# print(C.__mro__)