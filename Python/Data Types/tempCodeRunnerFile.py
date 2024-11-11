# A dictionary in Python is a built-in data structure that stores data in key-value pairs. It allows you to associate a 
# unique key with a specific value, enabling fast data retrieval and modification.

# li = [1,2]
# li1 = ["A","b"]

# print(dict(zip(li,li1)))

d = {1:"A",2:"B"}
print(d)

# Access
print(d[1])
print(d.get(1))

# display dictionary
print(d.items().mapping)

# All keys
print(d.keys())

# All keys values correspond to their key
print(d.values())

# Remove last key-value
# print(d.popitem())

#remove specific key-value
# print(d.pop(1))
# print(d)

d.setdefault(3,"C");
print(d)

d[3]="D"
print(d)

# User input
d1 = {}

l1 = []
l2 = []
for i in range(3):
    l1.append(int(input()))
    l2.append((input()))

d1 = dict(zip(l1,l2))
print(d1);
