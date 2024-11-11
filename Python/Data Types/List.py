#a list is a built-in data structure that allows you to store an ordered collection of items.
#Lists can contain elements of different data types,such as integers, strings, and even other
#lists.

# Key Characteristics of Lists:
# Ordered: Elements in a list have a defined order, and each element can be accessed using its index. The first element has an index of 0, 
# the second an index of 1, and so on.
# Mutable: Lists can be modified after their creation. You can change, add, or remove elements.
# Heterogeneous Elements: A list can contain elements of different types, such as numbers, strings, and even other lists.
# Dynamic: Lists can grow or shrink in size as you add or remove elements.

l = [1,2,1]

# Take input form user
li = []
n = int(input());
for i in range(n):
    ele = int(input())
    li.insert(i,ele)
print(li)

print(l)
#Access by index
print(l[0])
print(l[2])

print(l[-1])

#Add element at last
l.append(100)
print(l)

#add element ar particular index
l.insert(1,20)
print(l)

#remove particular index value if you not give any index then last element is gone
# l.pop(1)
# l.pop();
# print(l)

#return no of occurance
print(l.count(1))

# return first occurrence
print(l.index(1,1,len(l)))

# Delete all element
# l.clear()

#Copy all element on list to another list
l1 = l.copy()
# print(l1)

#Concat two list
# l.extend(l1);
# print(l)

#remove element by its value
# l.remove(1)
# print(l)

#reverse list
l.reverse()
print(l)

#sort list in descending manner
l.sort(reverse=True);
print(l)

# access specific part of the list
print(l[1::2])
print(l[-1::-2])