# continue: Skips the rest of the code in the current iteration and moves to the next iteration.

i = 2
j = 12

while i <= j:
    if i == 3:
        continue
    print(i)
    i += 1
