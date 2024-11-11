def divide(a,b):
    if b == 0:
        raise Exception("Denomintor Cannot Be Zero")
    else:
        print(a/b)

try:
    divide(1,0)
except Exception as e:
    print(e)