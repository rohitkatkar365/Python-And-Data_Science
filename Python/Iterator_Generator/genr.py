# What is a Generator?
# A generator is a special type of iterator in Python, defined using a function rather than a class. It allows you to iterate over a sequence of values lazily, meaning it generates values on-the-fly and does not store them in memory, making it very memory-efficient.

# Generators use the yield statement instead of return to produce a series of values one at a time. When the function is called, it returns a generator object without starting execution. When next() is called on the generator, the function runs until it hits a yield statement, returning the yielded value. The function’s state is preserved between successive calls.

# Example: Creating a Generator
# Here's how to create a simple generator that yields squares of numbers.

# python
# Copy code
# def square_numbers(n):
#     for i in range(n):
#         yield i * i

# # Creating a generator object
# squares = square_numbers(5)

# # Iterating over the generator
# for square in squares:
#     print(square)
# Output:

# Copy code
# 0
# 1
# 4
# 9
# 16
# Explanation:

# The square_numbers function uses yield to return square values one by one.
# Each time next() is called, it resumes execution from where it left off and continues until it hits the next yield statement.
# Key Differences Between Iterators and Generators
# Syntax and Creation:

# Iterators: Created using classes with __iter__() and __next__() methods.
# Generators: Created using functions with the yield keyword.
# Memory Usage:

# Iterators: Can consume more memory if all elements need to be stored.
# Generators: More memory-efficient as they yield items one at a time and do not store the entire sequence in memory.
# Execution:

# Iterators: Requires manual handling of state and stopping condition.
# Generators: Automatically handles state and stopping condition with yield and StopIteration.
# Convenience:

# Iterators: More verbose and requires more code to define.
# Generators: More concise and easy to define with yield.
# Use Cases for Generators
# Lazy Evaluation: Generators are ideal for situations where you don’t need to store the entire sequence in memory. For example, reading a large file line-by-line without loading the entire file into memory.

# Infinite Sequences: Generators can be used to create infinite sequences, like Fibonacci numbers or prime numbers, without running out of memory.

# Pipelining: Generators can be used to process data in a pipeline fashion. For example, chaining multiple generators together to process a data stream in stages.

# Example: Infinite Sequence with Generators
# Here's an example of a generator that generates an infinite sequence of Fibonacci numbers:

# python
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# # Creating a Fibonacci generator
# fib = fibonacci()

# # Printing the first 10 Fibonacci numbers
# for _ in range(10):
#     print(next(fib))
# Output:

# Copy code
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# Summary
# Iterators and Generators both provide a way to iterate over sequences of data, but they are created and used differently.
# Iterators require manual state management and stopping condition handling.
# Generators use the yield keyword, making them easier to use and more memory-efficient for large data streams.
# Both are fundamental to writing efficient and Pythonic code when dealing with sequences and data processing.