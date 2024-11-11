month = input("Enter Month :- ").lower()

match month:
    case "jan":
        print("Jan")
    case "feb":
        print("feb")
    case _:
        print("Enter valid month")
