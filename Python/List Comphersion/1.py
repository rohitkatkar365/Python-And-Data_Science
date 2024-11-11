# Comprehensions in Python provide a concise way to create lists, sets, and dictionaries. 
# They allow you to generate these collections by transforming or filtering items from existing iterables (like lists or sets) 
# in a single line of code.

li = [1,2,3,4,5,6,7,8,9,0]

even = [i for i in li if i%2==0]
print(even)
odd = [j for j in li if j%2!=0]
print(odd)