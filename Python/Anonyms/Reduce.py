# The reduce() function applies a binary function cumulatively to an iterable, reducing it to a single value.
# It is imported from the functools module and requires a function and an iterable as arguments.
# It can be used with a lambda function for concise syntax.
# An optional initializer can be provided to handle cases where the iterable is empty.

from functools import reduce

li = [1,2,3,4,5]

print(reduce(lambda a,b:a+b,li))