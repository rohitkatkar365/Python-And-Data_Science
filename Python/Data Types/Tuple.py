#a tuple is a built-in data structure that allows you to store an ordered collection of items.
#tuples can contain elements of different data types,such as integers, strings, and even other
#tuples.

# Key Characteristics of Tuples:
# Ordered: Tuples maintain the order of elements, meaning that the items have a defined position, and you can access them using their index.

# Immutable: Once a tuple is created, its elements cannot be modified, added, or removed. This immutability makes tuples suitable for 
# fixed collections of items.

# Heterogeneous Elements: Like lists, tuples can contain elements of different data types, such as integers, strings, floats, and 
# even other tuples.

# Faster Performance: Due to their immutability, tuples can be more memory-efficient and perform faster than lists, especially for 
# large collections of data.

# Hashable: Since tuples are immutable, they can be used as keys in dictionaries or as elements of sets, whereas lists cannot.

t = (1,2,3,1,4)

# print(t.count(1));
print(t.index(3))

# User Input
# t = ()
# l = []
# n = int(input("Enter Size Of Tuple :- "))
# for i in range(n):
#     ele = int(input("Enter Value :- "))
#     l.insert(i,ele);

# t = tuple(l);
# print(t)