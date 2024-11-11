# Exception handling is a programming concept used to manage errors that occur during the execution of a program. When an error occurs, the normal flow of the program is disrupted. The program creates an “exception” object that contains information about the error. The process of responding to this exception is called "exception handling"1.

# Key Components of Exception Handling:
# Try Block: The code that may potentially throw an exception is enclosed within a try block. If an exception occurs within this block, the control is transferred to the corresponding catch block.
# Catch Block: This block catches and handles the exceptions thrown within the try block. Each catch block is associated with a specific type of exception, allowing developers to handle different types of errors separately.
# Finally Block (Optional): The finally block is executed regardless of whether an exception occurs or not. It is commonly used to perform cleanup tasks, such as closing files or releasing resources

def divide(a,b):
    try:
        print(a // b)
    except Exception as e:
        print(e)

divide(1,0)