try:
    # Division that might cause a ZeroDivisionError
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result is: {result}")
finally:
    print("This will run no matter what.")
