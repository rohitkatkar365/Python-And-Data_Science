import multiprocessing

def square(n, res,val):
    val.value = 1.3
    for i, val in enumerate(n):
        res[i] = val * val  # Square the values from the list n

if __name__ == "__main__":
    li = [1, 2, 3, 4]  # List of numbers to square
    val = multiprocessing.Value("d",0.0)
    res = multiprocessing.Array("i", len(li))  # Shared array of integers
    
    # Pass the list and the shared result array to the process
    p1 = multiprocessing.Process(target=square, args=(li, res,val))

    p1.start()
    p1.join()

    # Print the squared values from the shared array
    print(res[:])  # Output will be: [1, 4, 9, 16]
    print(val.value)
