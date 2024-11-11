# Variable-Length Arguments: Use *args and **kwargs for flexible argument handling.

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)  # Output: 1 2 3 4

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  
# Output:
# name: Alice
# age: 25
