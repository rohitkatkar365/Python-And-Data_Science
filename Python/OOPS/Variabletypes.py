class A:
    # Class Vaiable
    wheel = 4
    def __init__(self,a):
        # // instance Vaiable
        self.a = A
        print(a)

a = A(10)
a.wheel = 5
print(a.wheel)
print(A.wheel)