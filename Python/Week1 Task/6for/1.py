# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

chead = 0;
for i in result:
    if i == "heads":
        chead+=1;

# print(chead);

# Print square of all numbers between 1 to 10 except even numbers
# for i in range(1,11):
#     if i % 2 == 0:
#            continue
#     print(i*i)

# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
#  If expense is not found then it should print that as well.

# expense_list = [2340, 2500, 2100, 3100, 2980]
# month_list = ["January", "February", "March", "April", "May"]
# expense_amount = int(input("Enter Expense Amount :- "));
# cnt = 0;
# for i in expense_list:
#     if(i == expense_amount):
#         print(month_list[cnt]);
#         break
#     cnt+=1;
# else:
#     print("Not Found");

# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
# for km in range(1, 6):
#     response = input(f"Completed {km} km. Are you tired? (yes/no): ").strip().lower()
#     if response == "yes":
#         print("You didn't finish the race.")
#         break
# else:
#     print("Congratulations! You finished the race.")

# *
# **
# ***
# ****
# *****
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()