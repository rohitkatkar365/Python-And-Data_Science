# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

city = input("Enter city name: ")

if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")

# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print
#  "They don't belong to same country"
city1 = input("Enter City Name1:- ").lower();
city2 = input("Enter City Name2:- ").lower();

if city1 in india and city2 in india:
    print(f"{city1} and {city2} Belong To Same india");
elif city1 in pakistan and city2 in pakistan:
    print(f"{city1} and {city2} Belong To Same pakistan");
elif city1 in bangladesh and city2 in bangladesh:
    print(f"{city1} and {city2} Belong To Same bangladesh");
else:
    print("Not Belong To Same Country")

# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")

