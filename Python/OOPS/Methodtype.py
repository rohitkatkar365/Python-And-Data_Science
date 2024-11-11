class Calculator:
    name = __name__
    def __init__(self):
        print("I am Calculator Class")
    
    def set(self,a,b):
        self.a = a
        self.b = b

    def get(self):
        self.c = self.a + self.b
        print(self.c)
    @classmethod
    def info(cls):
        print(cls.name)
    @staticmethod
    def fact(num):
        fact = 1
        while num != 0:
            fact *= num
            num-=1
        print(fact)

c1 = Calculator()
c1.set(1,2)
c1.get()
c1.fact(5)
c1.info()