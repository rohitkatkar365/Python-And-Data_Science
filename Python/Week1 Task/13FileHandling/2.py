input_file = "Week1 Task\\13FileHandling\\company_data.csv"
output_file = "Week1 Task\\13FileHandling\\output.csv"

with open(input_file, "r") as f, open(output_file, "w") as out:
    out.write("Company Name,PE Ratio,PB Ratio\n")
    next(f)  # Skip the header line
    for line in f:
        try:
            tokens = line.strip().split(",")
            stock = tokens[0]
            price = float(tokens[1])
            eps = float(tokens[2])
            book = float(tokens[3])
            pe = round(price / eps, 2)
            pb = round(price / book, 2)
            out.write(f"{stock},{pe},{pb}\n")
        except ValueError as e:
            print(f"Error processing line: {line.strip()} - {e}")
