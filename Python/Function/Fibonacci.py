def fib(n):
    a = 0
    b = 1
    print(f"{a} {b}",end=" ")
    fib = 0
    for i in range(2,n):
        c = a+b;
        fib +=c
        print(f"{c}",end=" ")
        a = b
        b = c

fib(6)