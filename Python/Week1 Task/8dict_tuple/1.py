# We have following information on countries and their population (population is in crores),

# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
info = dict({
    "China" : 143,
    "India" : 136,
    "USA" : 32,
    "Pakistan" : 21
})
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
userreq = input("User Request").lower()
if userreq == "print":  
    for i,j in info.items():
        print(f"{i}===>{j}")
elif userreq == "add":
    c = input("Enter Country :- ");
    if c in info:
        print("You Entered Country Already In Our Dictionay")
        exit
    else:
        p = int(input(f"Enter {c} Poupulation"));
        info[c] = p
        print(info)
elif userreq == "remove":
    c = input("Enter Country :- ");
    if c not in info:
        print("Country Not Available");
        exit
    else:
        del info[c]
        print(info)
elif userreq == "query":
    c = input("Enter Country :- ");
    if c not in info:
        print("Country Not Available");
        exit
    else:
        print(info[c])



