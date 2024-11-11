class DivByZero(Exception):
    def __init__(self, message="Denominator Cannot Be Zero"):
        super().__init__(message)

def div(a, b):
    try:
        if b == 0:
            raise DivByZero() 
        print(a / b)
    except DivByZero as e:
        print(e)

div(1, 0)
