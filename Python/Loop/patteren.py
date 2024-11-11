# *
# * *
# * * *

n = int(input())
# for i in range(0,n+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()

# * * * *
# * * *
# * *
# *

for i in range(n, 0,-1):
    for j in range(i):  # Change range to decrement from n
        print("*", end=" ")
    print()  # Move to the next line after each row
