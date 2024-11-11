# Swap two number

a = 1
b = 2

# 1 way
# temp = a;
# a = b;
# b = temp

# print(a,b)

# 2nd way
# a,b = b,a
# print(a,b)

# 3rd way
# a = a + b
# b = a - b
# a = a - b
# print(a,b)

# 4th way
a = a ^ b;  (1 ^ 2)
b = a ^ b;  (1 ^ 2) ^ 2  = 1   # xor cancel when 2 ^ 2 = 0
a = a ^ b;  (1 ^ 2) ^ 1 = 2    # xor cancel when 1 ^ 1 = 0
print(a,b) # 2 1