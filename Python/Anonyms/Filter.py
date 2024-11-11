li = [i for i in range(2, 11)]

# The filter() function filters elements from a list based on a condition defined in a function.
print(list(filter(lambda i : i % 2==0,li)))