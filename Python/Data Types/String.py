# What is String?
# String is a collection of character

# str = "Rohit"
# Python string is immutable
# str[0] = "A"
# print(str)

# Error : Traceback (most recent call last):
#   File "d:\Python and Data Science\Python\Data Types\String.py", line 7, in <module>
#     str[0] = "A"
#     ~~~^^^
# TypeError: 'str' object does not support item assignment


str1 = "     Rohit     "

# Access String
print(str1[0]) # Rohit

# Access String By Negative Index
print(str1[-1]) # t

# 1. Slicing : We Can Access Substring Using Slice
# Syntax : str1[start:end:step]
print(str1[0:3]) # Roh

# Reverse String
print(str1[-1::-1]) # titor

# 2. Strip() Return a copy of the string with the leading and trailing characters removed.
# 3./4. lstrip() for remove leading space and rstrip() for remove trailing space 
print(str1.strip()) # Rohit

# Remove #
s = '###hello###'.strip('#')
print(s) # hello

# 5./6. removeprefix() and removesuffix() : remove all occurrences of the passed chars string
s = 'Arthur: three!'.removeprefix('Arthur: ')
# 'three!'

s = 'HelloPython'.removesuffix('Python')
# 'Hello'

# 7. replace()
# Return a copy of the string with all occurrences of substring old replaced by new.
print("\n\nRam".replace("\n",""))

# 9. split()
# Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done.
str2 = "Vidyut Dev Singh Jammwal".split()
print(str2) #['Vidyut', 'Dev', 'Singh', 'Jammwal']

# 11. join()
# Return a string which is the concatenation of the strings in iterable.
s2 = " ".join(str2)
print(s2) # Vidyut Dev Singh Jammwal

# 12./13./14. upper(), lower(), capitalize().swapcase

print("ROHIT".lower()) # rohit
print("rohit".upper()) # ROHIT
print("rohit".capitalize()) # Rohit
print("Rohit".swapcase()) # rOHIT


# 15./16. islower(), isupper()
print(str1.islower()) # false
print(str1.isupper()) # false

# 17./18./19. isalpha(), isnumeric(), isalnum()
s = 'python'
print(s.isalpha(), s.isnumeric(), s.isalnum() )
# True False True

s = print(s.isalpha(), s.isnumeric(), s.isalnum() )
# False True True

s = 'python123'
print(s.isalpha(), s.isnumeric(), s.isalnum() )
# False False True

s = 'python-123'
print(s.isalpha(), s.isnumeric(), s.isalnum() )
# False False False

# 20. count()
# Return the number of non-overlapping occurrences of substring sub in the range [start, end].

n = 'hello world'.count('o') # 2

# 21. find()
# Return the lowest index in the string where substring sub is found within the slice s[start:end].

print("Machine Learning".find("a")) # return first a index
print("Machine Learning".find("a",2)) # return second a index

# 22. rfind()
print("Machine Learninga".rfind("a")) # return last occurrence index

# 23./24. startswith() and endswith()
print(str1.startswith("R")) # False
print(str1.endswith(" ")) # True

# 26./27./28 center(), ljust(), rjust()
s = 'Python is awesome!'
s = s.center(30, '-')
# ------Python is awesome!------

s = 'Python is awesome!'
s = s.ljust(30, '-')
# Python is awesome!------------

s = 'Python is awesome!'
s = s.rjust(30, '-')
# ------------Python is awesome!

