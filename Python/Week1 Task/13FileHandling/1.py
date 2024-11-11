word_d = {}

# Open the file in read mode
with open("Week1 Task\\13FileHandling\\poem.txt", "r") as f:
    # Read the file line by line
    for line in f:
        # Split each line into words
        words = line.split(" ")
        # Iterate over each word
        for word in words:
            # If the word is already in the dictionary, increment its count
            if word in word_d:
                word_d[word] += 1
            # If the word is not in the dictionary, add it with a count of 1
            else:
                word_d[word] = 1

# Convert dictionary values to a list to find maximum count
maxcnt = max(word_d.values())
print(f"Max Count :- {maxcnt}")

# Print words with the maximum count
print("Words with max occurrences are: ")
for word, cnt in word_d.items():
    if cnt == maxcnt:
        print(word)
