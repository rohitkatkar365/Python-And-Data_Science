# A set in Python is a built-in data structure that represents an unordered collection of unique elements.

# Key Characteristics of Sets:
# Unordered: The elements in a set do not have a defined order. When you iterate over a set, the items may appear in a different order
# each time.

# Unique Elements: Sets automatically eliminate duplicate values. Each element in a set must be unique; if you try to add a duplicate, 
# it will simply be ignored.

# Mutable: Sets can be modified after creation. You can add or remove elements, but the elements themselves must be immutable 
# (e.g., you cannot add a list or dictionary to a set).

# Dynamic Size: Sets can grow or shrink as you add or remove elements.

# Fast Membership Testing: Sets provide efficient membership testing, meaning you can quickly check whether an element is 
# part of the set.


# Take user input
# s = set()
# n = int(input())
# for i in range(n):
#     e = int(input())
#     s.add(e)
# print(s)

s = {1,1,2,3,4}
# print(s)

# Set difference
s1 = {1,3,7,9,0}
print(s.difference(s1))
# print(s1.difference(s))

#find common element 
print(s.intersection(s1))

#Union
print(s.union(s1));

# s.update(s1)
# print(s)

s.add(100)
print(s)

s.remove(100)
print(s)

