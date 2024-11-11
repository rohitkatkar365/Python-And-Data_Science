# What is an Iterator?
# An iterator is an object that can be iterated upon, meaning you can traverse through all the values contained within it. 
# It follows two main protocols:

# __iter__() Method: Returns the iterator object itself. This method is called when an iterator is initialized, allowing it to return 
# itself so that it can be used in a loop.

# __next__() Method: Returns the next value from the sequence. It raises a StopIteration exception when there are no more items to 
# return, signaling that the iteration is complete.

# How Does an Iterator Work?
# When you use an iterator in a loop or call the next() function, the __next__() method is invoked, and the next item is returned. 
# If there are no more items, StopIteration is raised, and the iteration stops.


class MyIerator:
    def __init__(self,data):
        self.data = data
        self.ind = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ind < len(self.data):
            result = self.data[self.ind]
            self.ind+=1
            return result
        else:
            raise StopIteration
    
iter = MyIerator([1,2,3,4,5])

for i in iter:
    print(i)
