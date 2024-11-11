# Lambda functions are anonymous functions defined with the lambda keyword.
# They can take multiple arguments and return the result of a single expression.
# Commonly used with built-in functions like map(), filter(), and sorted().
# Useful for short-lived functions where defining a full function would be unnecessary.

square = lambda a : a*a

add = lambda a,b : a+b

print(add(1,2))
print(square(2))