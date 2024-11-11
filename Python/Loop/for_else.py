# The for-else construct provides a clear and elegant way to handle scenarios where you want to distinguish between successful
# completion of a loop and early termination due to specific conditions. It enhances the readability of your code by 
# explicitly linking the else block to the loop's completion status

li = [1,2,3,4,5,6]
tar = 40
for i in li:
    if i == tar:
        print("Found")
        break
else:
    print("Not Found"); 