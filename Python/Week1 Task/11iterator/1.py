# <!-- ## Exercise: Iterators
# 1. Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
# 2. The iterator should stop when it reaches a `limit` defined in the constructor. -->

class Fib:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ind = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.ind >= self.c:
            raise StopIteration
        else:
            if self.ind == 0:
                self.ind += 1
                return self.a
            elif self.ind == 1:
                self.ind += 1
                return self.b
            else:
                self.a, self.b = self.b, self.a + self.b
                self.ind += 1
                return self.b

# Create an instance of Fib with the first two Fibonacci numbers 0, 1 and length 5
f1 = Fib(0, 1, 5)

# Iterate through the Fibonacci sequence
for i in f1:
    print(i)
