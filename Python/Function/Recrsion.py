# It is a phenomenon when a function calls itself indefinitely until a specified condition is fulfilled.

# reverse print list
# def pli(li,n):
#     if n <= 0:
#         return
#     print(li[n-1]);
#     pli(li,n-1)

# pli([1,2,3,4,5,6],len([1,2,3,4,5,6]))

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print(fact(5))